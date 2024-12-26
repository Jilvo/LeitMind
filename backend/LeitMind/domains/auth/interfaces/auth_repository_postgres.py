class AuthRepository:
    def __init__(self):
        """
        Initializes a new repository for managing prompts.
        """
        pass

    def create_user(self, username: str, email: str, hashed_password: str, country: str):
        pass

    def get_user_by_id(self, user_id: int):
        pass

    def get_all_users(self):
        pass

    def update_user(self, user_id: int, username: str, email: str, country: str):
        pass

    def delete_user(self, user_id: int):
        pass

    def get_user_by_email(self, email: str):
        pass

    def get_user_by_username(self, username: str):
        pass
