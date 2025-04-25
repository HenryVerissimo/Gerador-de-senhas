import string
from src.models.repositories.passwords_repository import PasswordsRepository

class PasswordsController:

    @staticmethod
    def insert_db(password: str) -> None:

        numbers = upper = lower = specials = False

        for caracter in password:
            if caracter in string.digits:
                numbers = True
            if caracter in string.ascii_uppercase:
                upper = True
            if caracter in string.ascii_lowercase:
                lower = True
            if caracter in string.punctuation:
                specials = True

        repository = PasswordsRepository()

        repository.insert_one(password, numbers, upper, lower, specials)
