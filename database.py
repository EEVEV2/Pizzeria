import sqlite3
from threading import Lock

class Database:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Database, cls).__new__(cls)
                cls._instance.connection = sqlite3.connect("pizzeria.db", check_same_thread=False)  # Połącz z pizzeria.db
                cls._instance.cursor = cls._instance.connection.cursor()
        return cls._instance

    def query(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor
