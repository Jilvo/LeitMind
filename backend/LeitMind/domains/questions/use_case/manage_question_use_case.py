from domains.auth.interfaces.auth_repository_postgres import AuthRepository
from domains.auth.schemas.user import UserCreationRequest
from domains.questions.interfaces.questions_repository_postgres import (
    QuestionsRepository,
)
from domains.questions.models.answer import Answer
from domains.questions.models.category import Category
from domains.questions.models.question import Question
from domains.questions.schemas.question import CategoryRequest, QuestionRequest
from kink import inject
from pydantic import ValidationError


@inject
class ManageQuestionUseCase:
    def __init__(self, questions_repository: QuestionsRepository):
        self.questions_repository = questions_repository
        self.auth_repository = AuthRepository()

    def create_question(self, question_data: QuestionRequest, current_user: UserCreationRequest):
        # Logique métier (si nécessaire)
        try:
            category: Category = self.questions_repository.get_category_by_id(question_data.category)
            if not category:
                raise ValueError("Category not found")
            user = self.auth_repository.get_user_by_email(current_user)
            question = Question(
                text=question_data.question,
                category_id=category.id,
                creator_id=user.id,
                explanation=question_data.explanation,
            )
            answers = []
            for index, aswr in enumerate(question_data.answers):
                answer = Answer(
                    is_correct=True if index == question_data.correct_answer else False,
                    question_id=question.id,
                    text=aswr,
                )
                answers.append(answer)
            self.questions_repository.create_question_with_answers(question, answers)
        except ValidationError as e:
            raise ValueError(f"Invalid data: {e}")

    def get_all_questions(self):
        """Get all questions."""
        return self.questions_repository.get_all_questions()

    def update_question(self, question_data: QuestionRequest):
        """Update a question."""
        category: Category = self.questions_repository.get_category_by_id(question_data.category)
        if not category:
            raise ValueError("Category not found")
        question = Question(
            id=question_data.id,
            text=question_data.question,
            category_id=category.id,
            explanation=question_data.explanation,
        )
        answers = []
        for index, aswr in enumerate(question_data.answers):
            answer = Answer(
                is_correct=True if index == question_data.correct_answer else False,
                question_id=question.id,
                text=aswr,
            )
            answers.append(answer)
        question = self.questions_repository.update_question(question)
        for answer in answers:
            self.questions_repository.update_answer(answer)
        return question

    def delete_question(self, question_id: int):
        """Delete a question."""
        return self.questions_repository.delete_question(question_id)

    def get_all_categories(self):
        """Get all categories."""
        return self.questions_repository.get_categories()

    def create_category(self, category_request: CategoryRequest):
        """Create a new category."""
        category = Category(name=category_request.name, description=category_request.description)
        return self.questions_repository.create_category(category)

    def update_category(self, category_id: int, category_name: str):
        """Update a category."""
        category = Category(id=category_id, name=category_name)
        return self.questions_repository.update_category(category)

    def delete_category(self, category_id: int):
        """Delete a category."""
        return self.questions_repository.delete_category(category_id)

    def get_questions_by_category(self, category_id: int):
        """Get all questions by category."""
        return self.questions_repository.get_questions_by_category(category_id)
