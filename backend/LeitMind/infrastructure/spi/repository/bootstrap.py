from infrastructure.spi.repository.auth_repository_postgres import (
    AuthRepositoryPostgreSQL,
)
from infrastructure.spi.repository.questions_repository_postgres import (
    QuestionsRepositoryPostgreSQL,
)


def bootstrap():
    questionsRepositoryPostgreSQL: QuestionsRepositoryPostgreSQL  # noqa: F842
    authRepositoryPostgreSQL: AuthRepositoryPostgreSQL  # noqa: F842
