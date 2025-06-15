from unittest.mock import MagicMock
from domains.questions.use_case.manage_category_use_case import ManageCategoryUseCase

def test_subscribe_to_category():
    mock_repo = MagicMock()
    use_case = ManageCategoryUseCase(questions_repository=mock_repo, auth_repository=MagicMock())
    
    use_case.subscribe_to_category_or_sub_category(category_id=1, sub_category_id=None, user_id=1)
    
    mock_repo.subscribe_to_category.assert_called_once_with(1, 1)

def test_subscribe_to_sub_category():
    mock_repo = MagicMock()
    use_case = ManageCategoryUseCase(questions_repository=mock_repo, auth_repository=MagicMock())
    
    use_case.subscribe_to_category_or_sub_category(category_id=None, sub_category_id=2, user_id=1)
    
    mock_repo.subscribe_to_sub_category.assert_called_once_with(2, 1)

def test_get_subscriptions_by_user():
    mock_repo = MagicMock()
    mock_repo.get_subscriptions_by_user.return_value = ["sub1", "sub2"]
    
    use_case = ManageCategoryUseCase(questions_repository=mock_repo, auth_repository=MagicMock())
    
    result = use_case.get_subscriptions_by_user(user_id=1)
    
    assert result == ["sub1", "sub2"]
    mock_repo.get_subscriptions_by_user.assert_called_once_with(1)

def test_remove_subscription():
    mock_repo = MagicMock()
    use_case = ManageCategoryUseCase(questions_repository=mock_repo, auth_repository=MagicMock())
    
    use_case.remove_subscription(category_id=1, sub_category_id=None, user_id=1)
    mock_repo.unsubscribe_from_category.assert_called_once_with(1, 1)