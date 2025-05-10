from domains.questions.models.attempt import Attempt
from infrastructure.spi.repository.database import SessionLocal
from kink import inject
from sqlalchemy import and_, not_, text
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.exc import NoResultFound

@inject(alias="attempt_repository")
@inject(alias="repository")
class AttemptRepositoryPostgreSQL:
    def __init__(self):
        """
        Initializes a new repository for managing attempts.
        """
        self.session = SessionLocal

    def get_all_attempts(self) -> list[dict]:
        with self.session() as session:
            attempts = session.query(Attempt).all()
            serialized_attempts = []
            for attempt in attempts:
                try:
                    serialized_attempts.append(attempt.to_dict())
                except Exception as e:
                    print(f"Error serializing attempt: {attempt}, Error: {e}")
            return serialized_attempts
    def get_attempt_by_id(self, attempt_id: int) -> Attempt:
        with self.session() as session:
            return (session.query(Attempt)
                .options(joinedload(Attempt.user))
                .filter(Attempt.id == attempt_id)
                .one()
            )
    def create_attempt(self, attempt: Attempt) -> Attempt:
        with self.session() as session:
            session.add(attempt)
            session.commit()
            session.refresh(attempt)
            return attempt
    def update_attempt(self, attempt: Attempt) -> Attempt:
        with self.session() as session:
            session.query(Attempt).filter(Attempt.id == attempt.id).update(
                attempt.to_dict())
            session.commit()
            session.refresh(attempt)
            return attempt
    def delete_attempt(self, attempt_id: str):
        with self.session() as session:
            attempt = session.query(Attempt).filter(
                Attempt.id == attempt_id
            ).delete()
            session.commit()
    def get_attempts_by_user_id(self, user_id: str) -> list[dict]:  
        with self.session() as session:
            attempts = (
                session.query(Attempt)
                .options(joinedload(Attempt.user))
                .filter(Attempt.user_id == user_id)
                .all()
            )
            serialized_attempts = []
            for attempt in attempts:
                try:
                    serialized_attempts.append(attempt.to_dict())
                except Exception as e:
                    print(f"Error serializing attempt: {attempt}, Error: {e}")
            return serialized_attempts
    def get_attempts_by_question_id(self, question_id: str) -> list[dict]:
        with self.session() as session:
            attempts = (
                session.query(Attempt)
                .options(joinedload(Attempt.question))
                .filter(Attempt.question_id == question_id)
                .all()
            )
            serialized_attempts = []
            for attempt in attempts:
                try:
                    serialized_attempts.append(attempt.to_dict())
                except Exception as e:
                    print(f"Error serializing attempt: {attempt}, Error: {e}")
            return serialized_attempts