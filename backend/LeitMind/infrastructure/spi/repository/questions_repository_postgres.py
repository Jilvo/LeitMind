from domains.questions.interfaces.questions_repository_postgres import QuestionsRepository
from domains.questions.models.answer import Answer
from domains.questions.models.category import Category
from domains.questions.models.question import Question
from domains.questions.models.sub_category import SubCategory
from domains.questions.models.theme import Theme
from infrastructure.spi.repository.database import SessionLocal
from kink import inject
from sqlalchemy.orm import joinedload


@inject(alias="questions_repository")
@inject(alias="repository")
class QuestionsRepositoryPostgreSQL(QuestionsRepository):
    def __init__(self):
        self.session = SessionLocal

    # Questions #
    def get_all_questions(self) -> list[Question]:
        with self.session() as session:
            questions = session.query(Question).all()
            return [question.to_dict() for question in questions]

    def get_question_by_id(self, question_id: int):
        with self.session() as session:
            return (
                session.query(Question)
                .options(joinedload(Question.answers))  # Charge les réponses en même temps
                .filter(Question.id == question_id)
                .first()
            )
            # return session.query(Question).filter(Question.id == question_id).first()

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

    def get_questions_by_question(self, category_id: int):
        with self.session() as session:
            return session.query(Question).filter(Question.category_id == category_id).all()

    def create_question(self, question: Question) -> Question:
        with self.session() as session:
            session.add(question)
            session.commit()
            session.refresh(question)
            return question

    def get_question_by_text(self, question_text: str) -> Question:
        with self.session() as session:
            return session.query(Question).filter(Question.text == question_text).first()

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

    def get_category_by_name(self, category: str) -> Category:
        with self.session() as session:
            return session.query(Category).filter(Category.name == category).first()

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

    def create_answer(self, answer) -> Answer:
        with self.session() as session:
            session.add(answer)
            session.commit()
            session.refresh(answer)
            return answer

    # Sub Categories #
    def create_sub_category(self, sub_category: SubCategory) -> SubCategory:
        with self.session() as session:
            session.add(sub_category)
            session.commit()
            session.refresh(sub_category)
            return sub_category

    def update_sub_category(self, sub_category_id: int, sub_category_name: str) -> SubCategory:
        with self.session() as session:
            session.query(SubCategory).filter(SubCategory.id == sub_category_id).update({"name": sub_category_name})
            session.commit()
            return self.get_sub_category_by_id(sub_category_id)

    def delete_sub_category(self, sub_category_id: int):
        with self.session() as session:
            session.query(SubCategory).filter(SubCategory.id == sub_category_id).delete()
            session.commit()

    def get_sub_categories_by_category(self, category_id: int) -> list[SubCategory]:
        with self.session() as session:
            return session.query(SubCategory).filter(SubCategory.category_id == category_id).all()

    def get_all_sub_categories(self) -> list[SubCategory]:
        with self.session() as session:
            return session.query(SubCategory).all()

    def get_sub_category_by_id(self, sub_category_id: int) -> SubCategory:
        with self.session() as session:
            return session.query(SubCategory).filter(SubCategory.id == sub_category_id).first()

    def get_sub_category_by_name(self, sub_category_name: str) -> SubCategory:
        with self.session() as session:
            return session.query(SubCategory).filter(SubCategory.name == sub_category_name).first()

    # Themes #
    def create_theme(self, theme) -> Theme:
        with self.session() as session:
            session.add(theme)
            session.commit()
            session.refresh(theme)
            return theme

    def update_theme(self, theme_id: int, theme_name: str) -> Theme:
        with self.session() as session:
            session.query(Theme).filter(Theme.id == theme_id).update({"name": theme_name})
            session.commit()
            return self.get_theme_by_id(theme_id)

    def delete_theme(self, theme_id: int):
        with self.session() as session:
            session.query(Theme).filter(Theme.id == theme_id).delete()
            session.commit()

    def get_themes(self) -> list[Theme]:
        with self.session() as session:
            themes = session.query(Theme).all()
            return [theme.to_dict() for theme in themes]

    def get_theme_by_id(self, theme_id: int) -> Theme:
        with self.session() as session:
            return session.query(Theme).filter(Theme.id == theme_id).first()

    def get_theme_by_name(self, theme_name: str) -> Theme:
        with self.session() as session:
            return session.query(Theme).filter(Theme.name == theme_name).first()

    def get_themes_by_sub_category(self, sub_category_id: int) -> list[Theme]:
        with self.session() as session:
            return session.query(Theme).filter(Theme.sub_category_id == sub_category_id).all()

    def get_questions_by_theme(self, theme_id: int) -> list[Question]:
        with self.session() as session:
            return session.query(Question).filter(Question.theme_id == theme_id).all()

    # Attempts #
    def create_attempt(self, attempt):
        with self.session() as session:
            session.add(attempt)
            session.commit()
            session.refresh(attempt)
            return attempt
