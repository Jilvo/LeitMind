from unittest.mock import MagicMock
from domains.questions.use_case.manage_attempt_use_case import ManageAttemptUseCase

def test_get_all_attempts():
    mock_repo = MagicMock()
    mock_repo.get_all_attempts.return_value = ["attempt1", "attempt2"]

    use_case = ManageAttemptUseCase(attempt_repository=mock_repo)
    result = use_case.get_all_attempts()

    assert result == ["attempt1", "attempt2"]
    mock_repo.get_all_attempts.assert_called_once()


def test_get_attempt_by_id():
    mock_repo = MagicMock()
    mock_repo.get_attempt_by_id.return_value = {"id": 1, "name": "attempt1"}

    use_case = ManageAttemptUseCase(attempt_repository=mock_repo)
    result = use_case.get_attempt_by_id(1)

    assert result == {"id": 1, "name": "attempt1"}
    mock_repo.get_attempt_by_id.assert_called_once_with(1)

def test_create_attempt():
    mock_repo = MagicMock()
    mock_attempt = {"name": "new_attempt"}
    mock_repo.create_attempt.return_value = {"id": 1, "name": "new_attempt"}

    use_case = ManageAttemptUseCase(attempt_repository=mock_repo)
    result = use_case.create_attempt(mock_attempt)

    assert result == {"id": 1, "name": "new_attempt"}
    mock_repo.create_attempt.assert_called_once_with(mock_attempt)
def test_update_attempt():
    mock_repo = MagicMock()
    mock_attempt = {"id": 1, "name": "updated_attempt"}
    mock_repo.update_attempt.return_value = {"id": 1, "name": "updated_attempt"}

    use_case = ManageAttemptUseCase(attempt_repository=mock_repo)
    result = use_case.update_attempt(mock_attempt)

    assert result == {"id": 1, "name": "updated_attempt"}
    mock_repo.update_attempt.assert_called_once_with(mock_attempt)
def test_delete_attempt():
    mock_repo = MagicMock()
    mock_repo.delete_attempt.return_value = None

    use_case = ManageAttemptUseCase(attempt_repository=mock_repo)
    result = use_case.delete_attempt(1)

    assert result is None
    mock_repo.delete_attempt.assert_called_once_with(1)
def test_get_attempts_by_user_id():
    mock_repo = MagicMock()
    mock_repo.get_attempts_by_user_id.return_value = [{"id": 1, "name": "attempt1"}]

    use_case = ManageAttemptUseCase(attempt_repository=mock_repo)
    result = use_case.get_attempts_by_user_id(1)

    assert result == [{"id": 1, "name": "attempt1"}]
    mock_repo.get_attempts_by_user_id.assert_called_once_with(1)

def test_get_attempts_by_question_id():
    mock_repo = MagicMock()
    mock_repo.get_attempts_by_question_id.return_value = [{"id": 1, "name": "attempt1"}]

    use_case = ManageAttemptUseCase(attempt_repository=mock_repo)
    result = use_case.get_attempts_by_question_id(1)

    assert result == [{"id": 1, "name": "attempt1"}]
    mock_repo.get_attempts_by_question_id.assert_called_once_with(1)