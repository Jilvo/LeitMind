from typing import Optional

from domains.questions.interfaces.subscription_repository_postgres import (
    SubscriptionRepository,
)
from domains.questions.models.subscription import UserSubscription

from infrastructure.spi.repository.database import SessionLocal
from kink import inject
from sqlalchemy import and_, not_, text
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.exc import NoResultFound


@inject(alias="subscription_repository")

class SubscriptionRepositoryPostgreSQL(SubscriptionRepository):
    def __init__(self):
        """
        Initializes a new repository for managing subscriptions.
        """
        self.session = SessionLocal

    def get_all_subscriptions(self) -> list[UserSubscription]:
        with self.session() as session:
            subscription = session.query(UserSubscription).all()
            return [subscription.to_dict() for subscription in subscription]
    def get_subscription_by_id(self, subscription_id):
        with self.session() as session:
            return (session.query(UserSubscription)
                .options(joinedload(UserSubscription.user))
                .filter(UserSubscription.id == subscription_id)
                .one()
            )
    def create_subscription(self, subscription: UserSubscription) -> UserSubscription:
        with self.session() as session:
            session.add(subscription)
            session.commit()
            session.refresh(subscription)
            return subscription
    def update_subscription(self, subscription: UserSubscription) -> UserSubscription:
        with self.session() as session:
            session.query(UserSubscription).filter(UserSubscription.id == subscription.id).update(
               subscription.to_dict())
            session.commit()
            session.refresh(subscription)
            return subscription
    def delete_subscription(self, subscription_id: str):
        with self.session() as session:
            subscription = session.query(UserSubscription).filter(
                UserSubscription.id == subscription_id
            ).delete()
            session.commit()
    def get_subscription_by_user_id(self, user_id: str) -> Optional[UserSubscription]:
        with self.session() as session:
                subscription = (
                    session.query(UserSubscription)
                    .options(joinedload(UserSubscription.user))
                    .filter(UserSubscription.user_id == user_id)
                    .one()
                )
                return subscription
    