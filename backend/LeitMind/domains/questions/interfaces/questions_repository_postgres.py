from domains.questions.models.answer import Answer
from domains.questions.models.category import Category
from domains.questions.models.question import Question


class QuestionsRepository:
    def __init__(self):
        """
        Initializes a new repository for managing prompts.
        """
        pass

    # Questions #
    def get_all_questions(self) -> list[Question]:
        """
        Get all questions.
        """
        pass

    def get_question_by_id(self, question_id: int) -> Question:
        """
        Get a question by ID.
        """
        pass

    def update_question(self, question: Question) -> Question:
        """
        Update a question.
        """
        pass

    def delete_question(self, question_id: int):
        """
        Delete a question.
        """
        pass

    def get_questions_by_category(self, category_id: int) -> list[Question]:
        """
        Get all questions by category.
        """
        pass

    # Categories #

    def get_categories(self) -> list[Category]:
        """
        Get all categories.
        """
        pass

    def get_category_by_id(self, category_id: int) -> Category:
        """
        Get a category by ID.
        """
        pass

    def create_category(self, category: Category) -> Category:
        """
        Create a new category.
        """
        pass

    def update_category(self, category: Category) -> Category:
        """
        Update a category.
        """
        pass

    def delete_category(self, category_id: int) -> None:
        """
        Delete a category.
        """
        pass

    # Answers #
    def create_question_with_answers(self, question: Question, answers: list[Answer]) -> Question:
        """
        Create a question with its answers.
        """
        pass

    def get_answers_by_question(self, question_id: int) -> list[Answer]:
        """
        Get all answers by question.
        """
        pass

    def update_answer(self, answer: Answer) -> Answer:
        """
        Update an answer.
        """
        pass

    def delete_answer(self, answer_id: int) -> None:
        """
        Delete an answer.
        """
        pass
