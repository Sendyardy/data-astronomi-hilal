from ..database.database import Database


class Pilih:
    def __init__(self):
        self.db_manager = Database()

    def pilih_tempat(self, nama_tempat: str):
        connection = self.db_manager.create_connection()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM tempat_observer WHERE nama_tempat LIKE ?",
                (f"%{nama_tempat}%",),
            )
            data = cursor.fetchone()
            connection.close()
            return data
