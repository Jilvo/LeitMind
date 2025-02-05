from domains.auth.interfaces.auth_repository_postgres import (
    AuthRepository,
)
from domains.auth.models.user import (
    User,
)
from infrastructure.spi.repository.database import (
    SessionLocal,
)
from kink import (
    inject,
)
from utils.security import (
    verify_password,
)


@inject(alias="auth_repository")
@inject(alias="repository")
class AuthRepositoryPostgreSQL(AuthRepository):
    def __init__(
        self,
    ):
        self.session = SessionLocal

    def create_user(
        self,
        user: User,
    ) -> User:
        if self.is_user_exist(
            user.username,
            user.email,
        ):
            raise ValueError("User already exists")
        with self.session() as session:

            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def get_user_by_id(
        self,
        user_id: int,
    ) -> User:
        with self.session() as session:
            return session.query(User).filter(User.id == user_id).first()

    def get_all_users(
        self,
    ):
        with self.session() as session:
            return session.query(User).all()

    def is_user_exist(
        self,
        username: str,
        email: str,
    ) -> bool:
        with self.session() as session:
            return session.query(User).filter(User.username == username).first() or session.query(User).filter(User.email == email).first()

    def update_user(
        self,
        user_id: int,
        username: str,
        email: str,
        country: str,
    ) -> User:
        with self.session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            user.username = username
            user.email = email
            user.country = country
            session.commit()
            session.refresh(user)
            return user

    def delete_user(
        self,
        user_id: int,
    ):
        with self.session() as session:
            session.query(User).filter(User.id == user_id).delete()
            session.commit()

    def get_user_by_email(
        self,
        email: str,
    ) -> User:
        with self.session() as session:
            return session.query(User).filter(User.email == email).first()

    def get_user_by_username(
        self,
        username: str,
    ) -> User:
        with self.session() as session:
            return session.query(User).filter(User.username == username).first()

    def authenticate_user(
        self,
        username: str,
        password: str,
    ) -> User:
        user = self.get_user_by_email(username)
        if not user:
            return False
        if not verify_password(
            password,
            user.hashed_password,
        ):
            return False
        return User(**user.to_dict())
