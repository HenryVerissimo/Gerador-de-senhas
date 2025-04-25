from os import getenv
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
host = getenv("HOST")
port = getenv("PORT")
user = getenv("USER")
password = getenv("PASSWORD")
database = getenv("DATABASE")

class ConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = f"mongodb://{user}:{password}@{host}:{port}"
        self.__client = None
        self.connection = None

    def create_connection(self) -> None:
        self.__client = MongoClient(self.__connection_string)
        self.connection = self.__client[database]

    def close_connection(self) -> None:
        self.__client.close()
        self.connection = None

    def __enter__(self) -> None:
        self.create_connection()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close_connection()
