from ..database.database import Database
from rich.console import Console


class Create:
    def __init__(self):
        self.db_manager = Database()

    def tambah_tempat(
        self,
        nama_tempat: str,
        lintang_tempat: float,
        bujur_tempat: float,
        ketinggian: float,
        time_zone: int,
    ):
        connection = self.db_manager.create_connection()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO tempat_observer (nama_tempat, lintang_tempat, bujur_tempat, ketinggian, time_zone) VALUES(?, ?, ?, ?, ?)",
                (nama_tempat, lintang_tempat, bujur_tempat, ketinggian, time_zone),
            )
            connection.commit()
            connection.close()
            console = Console()
            console.print("[green]Lokasi Tempat Berhasil Ditambahkan!![/green]")
