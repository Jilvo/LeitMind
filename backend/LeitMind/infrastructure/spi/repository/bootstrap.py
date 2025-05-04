from infrastructure.spi.repository.auth_repository_postgres import \
    AuthRepositoryPostgreSQL
from infrastructure.spi.repository.questions_repository_postgres import \
    QuestionsRepositoryPostgreSQL
from infrastructure.spi.repository.subscription_repository_postgres import \
    SubscriptionRepositoryPostgreSQL

def bootstrap():
    questionsRepositoryPostgreSQL: QuestionsRepositoryPostgreSQL  # noqa: F842
    authRepositoryPostgreSQL: AuthRepositoryPostgreSQL  # noqa: F842
    subscriptionRepositoryPostgreSQL: SubscriptionRepositoryPostgreSQL  # noqa: F842
