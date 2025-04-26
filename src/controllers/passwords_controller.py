import string
from src.models.repositories.passwords_repository import PasswordsRepository

class PasswordsController:
    def __init__(self) -> None:
        self.__repository = PasswordsRepository()

    def insert_db(self, password: str) -> None:

        if self.__repository.select_one(password):
            return False

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

        self.__repository.insert_one(password, numbers, upper, lower, specials)
        return True
