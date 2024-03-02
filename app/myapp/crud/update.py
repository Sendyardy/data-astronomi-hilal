from ..database.database import Database
from rich.console import Console


class Update:
    def __init__(self):
        self.db_manager = Database()

    def update_tempat(self, nama_tempat, new_data):
        connection = self.db_manager.create_connection()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE tempat_observer SET lintang_tempat=?, bujur_tempat=?, ketinggian=?, time_zone=? WHERE nama_tempat =?",
                (
                    new_data["lintang_tempat"],
                    new_data["bujur_tempat"],
                    new_data["ketinggian"],
                    new_data["time_zone"],
                    nama_tempat,
                ),
            )
            connection.commit()
            connection.close()
            console = Console()
            console.print(
                f"[green]Data Tempat Dengan Nama {nama_tempat} Berhasil Diperbaharui !!![/green]"
            )
