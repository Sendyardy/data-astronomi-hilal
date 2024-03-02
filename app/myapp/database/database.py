import sqlite3
from sqlite3 import Error


class Database:
    DATABASE_FILE = "datatempat.db"

    def create_connection(self):
        connection = None
        try:
            connection = sqlite3.connect(self.DATABASE_FILE)
            return connection
        except Error as e:
            print(e)

        return connection

    def creat_table(self):
        connection = self.create_connection()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS tempat_observer (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nama_tempat TEXT NOT NULL,
                    lintang_tempat REAL NOT NULL,
                    bujur_tempat REAL NOT NULL,
                    ketinggian  REAL NOT NULL,
                    time_zone INTEGER NOT NULL
                )
            """
            )
            connection.commit()
            connection.close()
