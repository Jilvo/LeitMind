from typing import Optional

from kink import inject
from sqlalchemy import and_, not_, text
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.exc import NoResultFound

from domains.auth.models.user import User
from domains.questions.interfaces.subscription_repository_postgres import \
    SubscriptionRepository
from domains.questions.models.subscription import UserSubscription
from infrastructure.spi.repository.database import SessionLocal


@inject(alias="subscription_repository")
class SubscriptionRepositoryPostgreSQL(SubscriptionRepository):
    def __init__(self):
        """
        Initializes a new repository for managing subscriptions.
        """
        self.session = SessionLocal

    def get_all_subscriptions(self) -> list[dict]:
        with self.session() as session:
            subscriptions = session.query(UserSubscription).all()
            serialized_subscriptions = []
        for subscription in subscriptions:
            try:
                serialized_subscriptions.append(subscription.to_dict())
            except Exception as e:
                print(f"Error serializing subscription: {subscription}, Error: {e}")
        return serialized_subscriptions

    def get_subscription_by_id(self, subscription_id: int) -> UserSubscription:
        with self.session() as session:
            return session.query(UserSubscription).options(joinedload(UserSubscription.user)).filter(UserSubscription.id == subscription_id).one()

    def create_subscription(self, subscription: UserSubscription) -> UserSubscription:
        with self.session() as session:
            session.add(subscription)
            session.commit()
            session.refresh(subscription)
            return subscription

    def update_subscription(self, subscription: UserSubscription) -> UserSubscription:
        with self.session() as session:
            session.query(UserSubscription).filter(UserSubscription.id == subscription.id).update(subscription.to_dict())
            session.commit()
            session.refresh(subscription)
            return subscription

    def delete_subscription(self, subscription_id: str):
        with self.session() as session:
            subscription = session.query(UserSubscription).filter(UserSubscription.id == subscription_id).delete()
            session.commit()

    def get_subscription_by_user_id(self, user_id: str) -> Optional[UserSubscription]:
        with self.session() as session:
            subscription = (
                session.query(UserSubscription).options(joinedload(UserSubscription.user)).filter(UserSubscription.user_id == user_id).one_or_none()
            )
            return subscription.to_dict() if subscription else None

    def count_subscriptions_by_sub_category(self, sub_category_id: str) -> dict:
        with self.session() as session:
            # Vérifiez si la sous-catégorie existe
            sub_category_exists = session.query(
                session.query(UserSubscription.sub_category_id).filter(UserSubscription.sub_category_id == sub_category_id).exists()
            ).scalar()

            if not sub_category_exists:
                raise ValueError(f"Sub-category with ID {sub_category_id} does not exist.")

            # Comptez les subscriptions actives pour cette sous-catégorie
            count = (
                session.query(UserSubscription)
                .filter(
                    and_(
                        UserSubscription.sub_category_id == sub_category_id,
                        not_(UserSubscription.is_active == 0),
                    )
                )
                .count()
            )

            # Récupérez les utilisateurs ayant souscrit à cette sous-catégorie
            users = (
                session.query(User)
                .join(UserSubscription, User.id == UserSubscription.user_id)
                .filter(UserSubscription.sub_category_id == sub_category_id)
                .all()
            )

            # Sérialisez les utilisateurs
            serialized_users = [user.to_dict() for user in users]

            return {
                "count": count,
                "users": serialized_users,
            }
