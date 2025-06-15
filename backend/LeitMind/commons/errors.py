class CategoryError(Exception):
    """Base class for all category-related errors."""

    pass


class QuestionError(Exception):
    """Base class for all question-related errors."""

    pass


class SubscriptionError(Exception):
    """Base class for all subscription-related errors."""

    pass


class UserError(Exception):
    """Base class for all user-related errors."""

    pass


class AttemptError(Exception):
    """Base class for all attempt-related errors."""

    pass


class AuthError(Exception):
    """Base class for all authentication-related errors."""

    pass


class QuizError(Exception):
    """Base class for all quiz-related errors."""

    pass


class QuestionNotFoundError(QuestionError):
    """Raised when a question is not found."""

    pass
