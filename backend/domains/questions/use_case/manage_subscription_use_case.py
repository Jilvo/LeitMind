import pandas as pd
from kink import inject
from pydantic import ValidationError

from domains.auth.interfaces.auth_repository_postgres import AuthRepository
from domains.auth.schemas.user import UserCreationRequest
from domains.questions.interfaces.questions_repository_postgres import \
    QuestionsRepository
from domains.questions.interfaces.subscription_repository_postgres import \
    SubscriptionRepository
from domains.questions.models.subscription import UserSubscription
from domains.questions.schemas.subscription import (SubscriptionRequest,
                                                    SubscriptionUserUpdateRequest)
from domains.questions.use_case.manage_question_use_case import \
    ManageQuestionUseCase


@inject
class ManageSubscriptionUseCase:
    def __init__(
        self,
        subscription_repository: SubscriptionRepository,
        manage_question_use_case: ManageQuestionUseCase,
        auth_repository: AuthRepository,
    ):
        """
        Initializes a new use case for managing subscriptions.
        """
        self.subscription_repository = subscription_repository
        self.auth_repository = auth_repository
        self.manage_question_use_case = manage_question_use_case

    def create_subscription(
        self,
        subscription_data: SubscriptionRequest,
        current_user: str,
    ) -> UserSubscription:
        """
        Create a new subscription.
        """
        try:
            user = self.auth_repository.get_user_by_email(current_user)
            # Validate the subscription data
            subscription = UserSubscription(
                user_id=user.id,
                category_id=subscription_data.category_id,  # Corrigé : category_id au lieu de sub_category_id
            )

            # Create the subscription
            return self.subscription_repository.create_subscription(subscription)
        except ValidationError as e:
            raise e
        except Exception as e:
            raise Exception(f"An error occurred while creating the subscription: {str(e)}")

    def get_all_subscriptions(
        self,
    ) -> list[dict]:
        """
        Get all subscriptions.
        """
        try:
            return self.subscription_repository.get_all_subscriptions()
        except Exception as e:
            raise Exception(f"An error occurred while retrieving subscriptions: {str(e)}")

    def get_subscription_by_id(
        self,
        subscription_id: str,
    ) -> UserSubscription:
        """
        Get a subscription by ID.
        """
        try:
            return self.subscription_repository.get_subscription_by_id(subscription_id)
        except Exception as e:
            raise Exception(f"An error occurred while retrieving the subscription: {str(e)}")

    def get_subscriptions_by_user_id(
        self,
        user_id: int,
    ) -> dict:
        """
        Get subscriptions by user ID formatted with categories and boolean values.
        """
        try:
            # Récupérer toutes les catégories disponibles
            all_categories = self.manage_question_use_case.get_all_categories()  # Tu dois implémenter cette méthode

            # Récupérer les souscriptions de l'utilisateur
            user_subscriptions = self.subscription_repository.get_subscriptions_by_user_id(user_id)

            # Créer un set des category_id auxquels l'utilisateur est abonné
            subscribed_category_ids = {sub["category_id"] for sub in user_subscriptions if sub["is_active"]}

            # Formater la réponse
            formatted_subscriptions = []
            for category in all_categories:
                formatted_subscriptions.append(
                    {
                        "category_id": category["id"],
                        "category_name": category["name"],  # Assure-toi que le nom existe dans ta table categories
                        "subscribed": category["id"] in subscribed_category_ids,
                    }
                )

            return {"message": "Subscriptions retrieved", "subscriptions": formatted_subscriptions}

        except Exception as e:
            raise Exception(f"An error occurred while retrieving subscriptions: {str(e)}")

    def count_subscriptions_by_sub_category(
        self,
        sub_category_id: int,
    ) -> int:
        """
        Count subscriptions by sub_category_id.
        """
        try:
            return self.subscription_repository.count_subscriptions_by_sub_category(sub_category_id)
        except Exception as e:
            raise Exception(f"An error occurred while counting subscriptions: {str(e)}")

    def delete_subscription(
        self,
        subscription_id: str,
    ) -> None:
        """
        Delete a subscription.
        """
        try:
            self.subscription_repository.delete_subscription(subscription_id)
        except Exception as e:
            raise Exception(f"An error occurred while deleting the subscription: {str(e)}")

    def update_subscriptions_by_user_id(
        self,
        user_id: int,
        subscription_data: SubscriptionUserUpdateRequest,
        current_user: str,
    ) -> dict:
        """
        Update subscriptions by user ID.
        Pour chaque catégorie dans la liste :
        - Si subscribed=True : créer ou activer la souscription
        - Si subscribed=False : désactiver la souscription (si elle existe)
        """
        try:
            user = self.auth_repository.get_user_by_email(current_user)
            if not user:
                raise Exception("User not found")
                
            if not subscription_data.subscriptions:
                raise ValidationError("No subscriptions provided")

            updated_count = 0
            
            # Traiter chaque souscription dans la liste
            for sub in subscription_data.subscriptions:
                if not isinstance(sub, SubscriptionRequest):
                    raise ValidationError("Invalid subscription data format")
                
                # Chercher si une souscription existe déjà pour cette catégorie
                existing_subscription = self.subscription_repository.get_subscription_by_user_and_category(
                    user_id, sub.category_id
                )
                
                if existing_subscription:
                    # La souscription existe déjà
                    if sub.subscribed != existing_subscription.is_active:
                        # L'état a changé, on met à jour
                        self.subscription_repository.update_subscription_by_id(
                            existing_subscription.id, 
                            {"is_active": sub.subscribed}
                        )
                        updated_count += 1
                else:
                    # Pas de souscription existante
                    if sub.subscribed:
                        # L'utilisateur veut s'abonner, on crée une nouvelle souscription
                        new_subscription = UserSubscription(
                            user_id=user_id,
                            category_id=sub.category_id,
                            is_active=True
                        )
                        self.subscription_repository.create_subscription(new_subscription)
                        updated_count += 1
                    # Si subscribed=False et pas de souscription existante, on ne fait rien

            return {
                "message": "Subscriptions updated successfully",
                "updated_count": updated_count,
                "total_processed": len(subscription_data.subscriptions)
            }
            
        except ValidationError as e:
            raise e
        except Exception as e:
            raise Exception(f"An error occurred while updating subscriptions: {str(e)}")
