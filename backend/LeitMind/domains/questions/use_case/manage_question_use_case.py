import pandas as pd
from kink import inject
from pydantic import ValidationError

from commons.errors import CategoryError
from domains.auth.interfaces.auth_repository_postgres import AuthRepository
from domains.auth.schemas.user import UserCreationRequest
from domains.questions.interfaces.questions_repository_postgres import \
    QuestionsRepository
from domains.questions.models.answer import Answer
from domains.questions.models.attempt import Attempt
from domains.questions.models.category import Category
from domains.questions.models.question import Question
from domains.questions.models.sub_category import SubCategory
from domains.questions.models.sub_theme import SubTheme
from domains.questions.models.theme import Theme
from domains.questions.schemas.question import (CategoryRequest,
                                                QuestionRequest,
                                                QuestionUpdateRequest,
                                                ValidateRequest)


@inject
class ManageQuestionUseCase:
    def __init__(
        self,
        questions_repository: QuestionsRepository,
        auth_repository: AuthRepository,
    ):
        self.questions_repository = questions_repository
        self.auth_repository = auth_repository

    def get_category_by_id(
        self,
        category_id: int,
    ) -> Category:
        """Get a category by id."""
        return self.questions_repository.get_category_by_id(category_id)

    def create_question(
        self,
        question_data: QuestionRequest,
        current_user: UserCreationRequest,
    ):
        try:
            category: Category = self.questions_repository.get_category_by_id(question_data.category)
            if not category:
                raise ValueError("Category not found")
            sub_category: SubCategory = self.questions_repository.get_sub_category_by_id(question_data.sub_category)
            if not sub_category:
                raise ValueError("Sub-category not found")

            theme: Theme = self.questions_repository.get_theme_by_id(question_data.theme)
            if not theme:
                raise ValueError("Theme not found")

            sub_theme: SubTheme = self.questions_repository.get_sub_theme_by_id(question_data.sub_theme)

            if not sub_theme:
                raise ValueError("Sub-theme not found")

            user = self.auth_repository.get_user_by_email(current_user)
            question = Question(
                text=question_data.text,
                category_id=category.id,
                theme_id=theme.id,
                sub_theme_id=sub_theme.id,
                creator_id=user.id,
                explanation=question_data.explanation,
            )
            answers = []
            for (
                index,
                aswr,
            ) in enumerate(question_data.answers):
                answer = Answer(
                    is_correct=(True if index == question_data.correct_answer else False),
                    question_id=question.id,
                    text=aswr,
                )
                answers.append(answer)
            self.questions_repository.create_question_with_answers(
                question,
                answers,
            )
        except ValidationError as e:
            raise ValueError(f"Invalid data: {e}")

    def get_all_questions(
        self,
    ) -> list[Question]:
        """Get all questions."""
        try:
            questions = self.questions_repository.get_all_questions()
            print(f"Questions brutes du repo: {len(questions)}")

            return questions[:5]

        except Exception as e:
            print(f"Erreur dans get_all_questions du use case: {str(e)}")
            import traceback

            traceback.print_exc()
            return []

    def update_question(
        self,
        question_id: int,
        question_data: QuestionUpdateRequest,
        current_user: str,
    ):
        """Update a question."""
        try:
            print(f"Updating question with ID: {question_id}")
            print(f"Question data: {question_data}")
            print(f"Current user: {current_user}")

            question = self.questions_repository.get_question_by_id(question_id)
            print(f"Type of question: {type(question)}")
            if not question:
                raise ValueError("Question not found")
            print(f"Existing question: {question}")

            category = self.questions_repository.get_category_by_id(question_data.category)
            print(f"Type of category: {type(category)}")
            if not category:
                raise CategoryError("Category not found for this question. You must create it first.")

            question.text = question_data.text
            question.category_id = category.id
            question.explanation = question_data.explanation

            old_answers = self.questions_repository.get_answers_by_question(question_id)
            for old_answer in old_answers:
                self.questions_repository.delete_answer(old_answer.id)

            for (
                index,
                aswr,
            ) in enumerate(question_data.answers):
                answer = Answer(
                    is_correct=(True if index == question_data.correct_answer else False),
                    question_id=question.id,
                    text=aswr,
                )
                self.questions_repository.create_answer(answer)
            print(f"Question updated successfully: {question}")

            return question
        except Exception as e:
            print(f"Error during question update: {e}")
            raise ValueError(f"Failed to update question: {e}")

    def delete_question(
        self,
        question_id: int,
    ):
        """Delete a question."""
        return self.questions_repository.delete_question(question_id)

    def get_all_categories(
        self,
    ):
        """Get all categories."""
        return self.questions_repository.get_categories()

    def create_category(
        self,
        category_request: CategoryRequest,
    ) -> CategoryRequest:
        """Create a new category."""
        category = Category(
            name=category_request.name,
            description=category_request.description,
        )
        return self.questions_repository.create_category(category)

    def update_category(
        self,
        category_id: int,
        category_name: str,
    ):
        """Update a category."""
        category = Category(
            id=category_id,
            name=category_name,
        )
        return self.questions_repository.update_category(category)

    def delete_category(
        self,
        category_id: int,
    ):
        """Delete a category."""
        return self.questions_repository.delete_category(category_id)

    def get_questions_by_category(
        self,
        category_id: int,
    ):
        """Get all questions by category."""
        return self.questions_repository.get_questions_by_category(category_id)

    def create_sub_category(
        self,
        sub_category: SubCategory,
    ) -> SubCategory:
        """Create a new sub category."""
        return self.questions_repository.create_sub_category(sub_category)

    def update_sub_category(
        self,
        sub_category_id: int,
        sub_category_name: str,
    ):
        """Update a sub category."""
        return self.questions_repository.update_sub_category(
            sub_category_id,
            sub_category_name,
        )

    def delete_sub_category(
        self,
        sub_category_id: int,
    ):
        """Delete a sub category."""
        return self.questions_repository.delete_sub_category(sub_category_id)

    def get_sub_categories_by_category(
        self,
        category_id: int,
    ):
        """Get all sub categories by category."""
        return self.questions_repository.get_sub_categories_by_category(category_id)

    def get_all_sub_categories(
        self,
    ):
        """Get all sub categories."""
        return self.questions_repository.get_all_sub_categories()

    def get_sub_category_by_id(
        self,
        sub_category_id: int,
    ):
        """Get a sub category by id."""
        return self.questions_repository.get_sub_category_by_id(sub_category_id)

    def get_sub_category_by_name(
        self,
        sub_category_name: str,
    ):
        """Get a sub category by name."""
        return self.questions_repository.get_sub_category_by_name(sub_category_name)

    def get_themes(
        self,
    ):
        """Get all themes."""
        return self.questions_repository.get_themes()

    def get_theme_by_id(
        self,
        theme_id: int,
    ):
        """Get a theme by id."""
        return self.questions_repository.get_theme_by_id(theme_id)

    def get_theme_by_name(
        self,
        theme_name: str,
    ):
        """Get a theme by name."""
        return self.questions_repository.get_theme_by_name(theme_name)

    def create_theme(
        self,
        theme: Theme,
    ) -> Theme:
        """Create a new theme."""
        return self.questions_repository.create_theme(theme)

    def update_theme(
        self,
        theme_id: int,
        theme_name: str,
    ):
        """Update a theme."""
        return self.questions_repository.update_theme(
            theme_id,
            theme_name,
        )

    def delete_theme(
        self,
        theme_id: int,
    ):
        """Delete a theme."""
        return self.questions_repository.delete_theme(theme_id)

    def get_themes_by_sub_category(
        self,
        sub_category_id: int,
    ):
        """Get all themes by sub category."""
        return self.questions_repository.get_themes_by_sub_category(sub_category_id)

    def get_questions_by_theme(
        self,
        theme_id: int,
    ):
        """Get all questions by theme."""
        return self.questions_repository.get_questions_by_theme(theme_id)

    def get_category_by_name(
        self,
        category: str,
    ) -> Category:
        """Get a category by name."""
        return self.questions_repository.get_category_by_name(category)

    def bulk_create_questions(
        self,
    ):
        """Bulk create questions."""
        try:
            # Lire le fichier CSV
            df = pd.read_csv("datas/question_dot.csv", quotechar='"', on_bad_lines="skip", delimiter=";")
            df_head = df.head()
            print(df_head)
            for (
                index,
                row,
            ) in df.iterrows():
                print(index)
                # print(row)
                # print(row)
                category = self.get_category_by_name(row["category"])
                if not category:
                    category = Category(name=row["category"])
                    category = self.create_category(category)
                sub_category = self.get_sub_category_by_name(row["sub_category"])
                if not sub_category:
                    sub_category = SubCategory(
                        name=row["sub_category"],
                        category_id=category.id,
                    )
                    sub_category = self.create_sub_category(sub_category)
                theme = self.get_theme_by_name(row["theme"])
                if not theme:
                    theme = Theme(
                        name=row["theme"],
                        sub_category_id=sub_category.id,
                    )
                    theme = self.create_theme(theme)
                sub_theme = self.questions_repository.get_sub_theme_by_name(row["sub_theme"])
                if not sub_theme:
                    sub_theme = SubTheme(
                        name=row["sub_theme"],
                    )
                    sub_theme = self.questions_repository.create_sub_theme(sub_theme)
                question = Question(
                    text=row["question"],
                    category_id=category.id,
                    theme_id=theme.id,
                    sub_theme_id=sub_theme.id,
                    creator_id=1,
                    explanation=row["explanation"],
                )
                question_already_exists = self.questions_repository.get_question_by_text(question.text)
                if question_already_exists:
                    continue
                question = self.questions_repository.create_question(question)
                answers = []
                answers_possibility = [
                    row["answer_1"],
                    row["answer_2"],
                    row["answer_3"],
                ]
                for (
                    index,
                    aswr,
                ) in enumerate(answers_possibility):
                    answer = Answer(
                        is_correct=(True if index + 1 == row["index_correct_answer"] else False),
                        question_id=question.id,
                        text=aswr.replace(
                            "\n",
                            "",
                        )
                        .replace(
                            "\r",
                            "",
                        )
                        .replace(
                            "\t",
                            "",
                        )
                        .replace(
                            "  ",
                            " ",
                        )
                        .replace(
                            '"',
                            "",
                        ),
                    )
                    answers.append(answer)
                    self.questions_repository.create_answer(answer)
                # self.questions_repository.create_question_with_answers(
                #     question, answers
                # )
                print(question)
            print(df.head())
            a = df.head().to_dict("records")
            return a
        except Exception as e:
            print(f"Error reading CSV file: {e}")
        return None
        # return self.questions_repository.bulk_create_questions()

    def get_question_by_id(
        self,
        question_id: int,
    ) -> dict:
        """Get a question by id with answers."""
        question = self.questions_repository.get_question_by_id(question_id).to_dict()
        aswrs = self.questions_repository.get_answers_by_question(question_id)
        answers = [aswr.to_dict() for aswr in aswrs]
        return {
            "question": question,
            "answers": answers,
        }

    # Validation
    def validate_question(
        self,
        validation_data: ValidateRequest,
        current_user: str,
    ):
        """Validate a question."""
        question: Question = self.questions_repository.get_question_by_id(validation_data.question_id)
        if not question:
            raise ValueError("Question not found")
        answers = question.answers
        correct_answer = [answer for answer in answers if answer.is_correct]
        is_correct = False
        if validation_data.answer_id == correct_answer[0].id:
            is_correct = True
        user = self.auth_repository.get_user_by_email(current_user)
        attempt = self.questions_repository.get_attempt_by_question_and_user_id(
            question.id,
            user.id,
        )
        if not attempt:
            attempt = Attempt(
                question_id=question.id,
                user_id=user.id,
                is_correct=is_correct,
                answer_id=validation_data.answer_id,
                # attempt_count=1,
                # leitner_box=1,
            )
        else:
            # TODO si faux leitner box revient à 1 sinon sinon +1 select_daily_quiz_use_case.py::get_outdated_attempts
            attempt.leitner_box += 1
            attempt.attempt_count += 1
            attempt.is_correct = is_correct
            attempt.answer_id = validation_data.answer_id
        self.questions_repository.create_or_update_attempt(
            attempt,
            # current_user,
        )
        if is_correct:
            return (
                "Correct answer",
                "",
            )
        return (
            "Bad answer",
            question.explanation,
        )

    def get_correct_answer(
        self,
        question_id: int,
    ):
        """Get the correct answer for a question."""
        question = self.questions_repository.get_question_by_id(question_id)
        if not question:
            raise ValueError("Question not found")
        answers = question.answers
        correct_answer = [answer for answer in answers if answer.is_correct]
        if not correct_answer:
            raise ValueError("No correct answer found")
        return correct_answer[0].text
