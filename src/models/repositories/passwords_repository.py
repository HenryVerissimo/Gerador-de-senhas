from os import getenv
from dotenv import load_dotenv
from src.models.configs.connection import ConnectionHandler

load_dotenv()
collection = getenv("COLLECTION")

class PasswordsRepository:
    
    def insert_one(self, password: str, numbers:bool, lirics_upper:bool, lirics_lower:bool, specials:bool) -> bool:
            with ConnectionHandler() as db:
                document = {"password": password, "numbers": numbers, "lirics": {"upper": lirics_upper, "lower": lirics_lower}, "specials": specials}
                cursor = db.connection[collection]
                cursor.insert_one(document)
                return True

