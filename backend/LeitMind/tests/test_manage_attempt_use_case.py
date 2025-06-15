from unittest.mock import MagicMock
from domains.questions.use_case.manage_attempt_use_case import ManageAttemptUseCase

def test_get_all_attempts():
    mock_repo = MagicMock()
    mock_repo.get_all_attempts.return_value = ["attempt1", "attempt2"]

    use_case = ManageAttemptUseCase(attempt_repository=mock_repo)
    result = use_case.get_all_attempts()

    assert result == ["attempt1", "attempt2"]
    mock_repo.get_all_attempts.assert_called_once()