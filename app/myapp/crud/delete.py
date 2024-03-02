from ..database.database import Database
from rich.console import Console


class Delete:
    def __init__(self):
        self.db_manager = Database()

    def hapus_tempat(self, nama_tempat: str):
        connection = self.db_manager.create_connection()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute(
                "DELETE FROM tempat_observer WHERE nama_tempat= ?", (nama_tempat,)
            )
            connection.commit()
            connection.close()
            console = Console()
            console.print("[yellow] Tempat Berhasil Dihapus!!![/yellow]")
