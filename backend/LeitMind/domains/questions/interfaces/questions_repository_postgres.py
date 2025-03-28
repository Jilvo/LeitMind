from domains.questions.models.answer import Answer
from domains.questions.models.attempt import Attempt
from domains.questions.models.category import Category
from domains.questions.models.question import Question
from domains.questions.models.sub_category import SubCategory
from domains.questions.models.theme import Theme


class QuestionsRepository:
    def __init__(
        self,
    ):
        """
        Initializes a new repository for managing prompts.
        """
        pass

    # Questions #
    def get_all_questions(
        self,
    ) -> list[Question]:
        """
        Get all questions.
        """
        pass

    def get_question_by_id(
        self,
        question_id: int,
    ) -> Question:
        """
        Get a question by ID.
        """
        pass

    def create_question(
        self,
        question: Question,
    ) -> Question:
        """
        Create a new question.
        """
        pass

    def update_question(
        self,
        question: Question,
    ) -> Question:
        """
        Update a question.
        """
        pass

    def delete_question(
        self,
        question_id: int,
    ):
        """
        Delete a question.
        """
        pass

    def get_question_by_text(
        text: str,
    ) -> Question:
        """
        Get a question by text.
        """
        pass

    def get_questions_by_category(
        self,
        category_id: int,
    ) -> list[Question]:
        """
        Get all questions by category.
        """
        pass

    def get_questions_by_ids(
        self,
        question_ids: list[int],
    ) -> list[Question]:
        """
        Get all questions by IDs.
        """
        pass

    def get_unattempted_questions_by_user_id(
        self,
        user_id: int,
    ) -> list[Question]:
        """
        Get all unattempted questions by user ID.
        """
        pass

    def get_unattempted_questions_by_user_id_and_subscribed_sub_categories(
        self,
        user_id: int,
        list_id_sub_categories: list[int],
    ) -> list[Question]:
        """
        Get all unattempted questions by user ID and categories ID which User subscribed to.
        """
        pass

    def get_unattempted_questions_by_user_id_and_sub_category_choosed(
        self,
        user_id: int,
        theme_id: int,
    ) -> list[Question]:
        """
        Get all unattempted questions by user ID and theme ID.
        """
        pass

    # Categories #

    def get_categories(
        self,
    ) -> list[Category]:
        """
        Get all categories.
        """
        pass

    def get_category_by_id(
        self,
        category_id: int,
    ) -> Category:
        """
        Get a category by ID.
        """
        pass

    def create_category(
        self,
        category: Category,
    ) -> Category:
        """
        Create a new category.
        """
        pass

    def update_category(
        self,
        category: Category,
    ) -> Category:
        """
        Update a category.
        """
        pass

    def delete_category(
        self,
        category_id: int,
    ) -> None:
        """
        Delete a category.
        """
        pass

    def get_category_by_name(
        self,
        category_name: str,
    ) -> Category:
        """
        Get a category by name.
        """
        pass

    def get_all_categories(
        self,
    ) -> list[Category]:
        """
        Get all categories.
        """
        pass

    # Answers #
    def create_question_with_answers(
        self,
        question: Question,
        answers: list[Answer],
    ) -> Question:
        """
        Create a question with its answers.
        """
        pass

    def get_answers_by_question(
        self,
        question_id: int,
    ) -> list[Answer]:
        """
        Get all answers by question.
        """
        pass

    def update_answer(
        self,
        answer: Answer,
    ) -> Answer:
        """
        Update an answer.
        """
        pass

    def delete_answer(
        self,
        answer_id: int,
    ) -> None:
        """
        Delete an answer.
        """
        pass

    # Sub Categories #
    def create_sub_category(
        self,
        sub_category: SubCategory,
    ) -> SubCategory:
        """
        Create a new sub category.
        """
        pass

    def update_sub_category(
        self,
        sub_category_id: int,
        sub_category_name: str,
    ) -> SubCategory:
        """
        Update a sub category.
        """
        pass

    def delete_sub_category(
        self,
        sub_category_id: int,
    ):
        """
        Delete a sub category.
        """
        pass

    def get_sub_categories_by_category(
        self,
        category_id: int,
    ):
        """
        Get all sub categories by category.
        """
        pass

    def get_all_sub_categories(
        self,
    ) -> list[SubCategory]:
        """
        Get all sub categories.
        """
        pass

    def get_sub_category_by_id(
        self,
        sub_category_id: int,
    ) -> SubCategory:
        """
        Get a sub category by id.
        """
        pass

    def get_sub_category_by_name(
        self,
        sub_category_name: str,
    ) -> SubCategory:
        """
        Get a sub category by name.
        """
        pass

    # Themes #
    def create_theme(
        self,
        theme,
    ) -> Theme:
        """
        Create a new theme.
        """
        pass

    def update_theme(
        self,
        theme_id: int,
        theme_name: str,
    ) -> Theme:
        """
        Update a theme.
        """
        pass

    def delete_theme(
        self,
        theme_id: int,
    ):
        """
        Delete a theme.
        """
        pass

    def get_themes(
        self,
    ) -> list[Theme]:
        """
        Get all themes.
        """
        pass

    def get_theme_by_id(
        self,
        theme_id: int,
    ) -> Theme:
        """
        Get a theme by id.
        """
        pass

    def get_theme_by_name(
        self,
        theme_name: str,
    ) -> Theme:
        """
        Get a theme by name.
        """
        pass

    def get_themes_by_sub_category(
        self,
        sub_category_id: int,
    ) -> list[Theme]:
        """
        Get all themes by sub category.
        """
        pass

    def get_questions_by_theme(
        self,
        theme_id: int,
    ) -> list[Question]:
        """
        Get all questions by theme.
        """
        pass

    def create_answer(
        answer,
    ) -> Answer:
        """
        Create a new answer.
        """
        pass

    # Attempts
    def create_or_update_attempt(
        self,
        attempt,
    ) -> Attempt:
        """
        Create or Update a new attempt.
        """
        pass

    def get_attempt_by_id(
        self,
        attempt_id: int,
    ) -> Attempt:
        """
        Get an attempt by ID.
        """
        pass

    def get_attempt_by_question_and_user_id(
        self,
        question_id: int,
        user_id: int,
    ) -> Attempt:
        """
        Get an attempt by question and user ID.
        """
        pass

    def get_all_attempts_by_user_id(
        self,
        user_id: int,
    ) -> list[Attempt]:
        """
        Get all attempts by user ID.
        """
        pass

    # Subscriptions

    def subscribe_to_category(
        self,
        category_id: int,
        user_id: int,
    ) -> None:
        """
        Subscribe to a category.
        """
        pass

    def subscribe_to_sub_category(
        self,
        sub_category_id: int,
        user_id: int,
    ) -> None:
        """
        Subscribe to a sub category.
        """
        pass

    def get_subscriptions_by_user(
        self,
        user_id: int,
    ) -> list[Category]:
        """
        Get all subscriptions by user ID.
        """
        pass

    def unsubscribe_from_category(
        self,
        category_id: int,
        user_id: int,
    ) -> None:
        """
        Unsubscribe from a category.
        """
        pass

    def unsubscribe_from_sub_category(
        self,
        sub_category_id: int,
        user_id: int,
    ) -> None:
        """
        Unsubscribe from a sub category.
        """
        pass
