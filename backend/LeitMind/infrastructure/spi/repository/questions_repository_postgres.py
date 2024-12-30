from domains.questions.interfaces.questions_repository_postgres import (
    QuestionsRepository,
)
from domains.questions.models.answer import Answer
from domains.questions.models.category import Category
from domains.questions.models.question import Question
from infrastructure.spi.repository.database import SessionLocal
from kink import inject


@inject(alias="questions_repository")
@inject(alias="repository")
class QuestionsRepositoryPostgreSQL(QuestionsRepository):
    def __init__(self):
        self.session = SessionLocal

    # Questions #
    def get_all_questions(self):
        with self.session() as session:
            return session.query(Question).all()

    def get_question_by_id(self, question_id: int):
        with self.session() as session:
            return session.query(Question).filter(Question.id == question_id).first()

    def update_question(self, question: Question):
        with self.session() as session:
            session.query(Question).filter(Question.id == question.id).update(question.to_dict())
            session.commit()
            session.refresh(question)
            return question

    def delete_question(self, question_id: int):
        with self.session() as session:
            session.query(Question).filter(Question.id == question_id).delete()
            session.commit()

    def get_questions_by_category(self, category_id: int):
        with self.session() as session:
            return session.query(Question).filter(Question.category_id == category_id).all()

    # Categories #
    def get_categories(self) -> list[Category]:
        with self.session() as session:
            categories = session.query(Category).all()
            return [category.to_dict() for category in categories]

    def get_category_by_id(self, category_id: int) -> Category:
        with self.session() as session:
            return session.query(Category).filter(Category.id == category_id).first()

    def create_category(self, category: Category) -> Category:
        with self.session() as session:
            session.add(category)
            session.commit()
            session.refresh(category)
            return category

    def update_category(self, category: Category) -> Category:
        with self.session() as session:
            session.query(Category).filter(Category.id == category.id).update(category.to_dict())
            session.commit()
            session.refresh(category)
            return category

    def delete_category(self, category_id: int) -> None:
        with self.session() as session:
            session.query(Category).filter(Category.id == category_id).delete()
            session.commit()

    # Answers #
    def create_question_with_answers(self, question: Question, answers: list[Answer]) -> Question:
        with self.session() as session:
            session.add(question)
            session.commit()
            session.refresh(question)
            for answer in answers:
                answer.question_id = question.id
                session.add(answer)
            session.commit()
            session.refresh(question)
            return question

    def get_answers_by_question(self, question_id: int) -> list[Answer]:
        with self.session() as session:
            return session.query(Answer).filter(Answer.question_id == question_id).all()

    def update_answer(self, answer: Answer) -> Answer:
        with self.session() as session:
            session.query(Answer).filter(Answer.id == answer.id).update(answer.to_dict())
            session.commit()
            session.refresh(answer)
            return answer

    def delete_answer(self, answer_id):
        with self.session() as session:
            session.query(Answer).filter(Answer.id == answer_id).delete()
            session.commit()
