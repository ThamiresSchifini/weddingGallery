from src.models import User


class AuthService:
    """This is a fake auth service, to simulate a token-based authentication."""

    @staticmethod
    def check_password(user: User, password: str) -> bool:
        return AuthService._hash_password(password) == user.password

    @staticmethod
    def make_token(user: User) -> str:
        token = str(user._id) * 3
        return token

    @staticmethod
    def user_id_from_token(token: str) -> str:
        return token[:len(token) // 3]

    @staticmethod
    def check_token(user: User, token: str) -> bool:
        return AuthService.make_token(user) == token

    @staticmethod
    def _hash_password(password: str) -> str:
        upper_password = password.upper()

        letter_to_number = upper_password \
            .replace('A', '4') \
            .replace('I', '1') \
            .replace('O', '0')

        return letter_to_number * 3
