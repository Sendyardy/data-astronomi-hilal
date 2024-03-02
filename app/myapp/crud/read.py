from ..database.database import Database
from rich.console import Console
from rich.table import Table


class Read:
    def __init__(self):
        self.db_manager = Database()

    def lihat_tempat(self):
        connection = self.db_manager.create_connection()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM tempat_observer")
            rows = cursor.fetchall()
            connection.close()

            if not rows:
                console = Console()
                console.print(
                    "[red] Data Tempat Kosong. Tidak ada data yang ditampilkan????[/red]"
                )
                return

            table = Table(
                title="Daftar Tempat", show_header=True, header_style="bold magenta"
            )
            table.add_column("Nama Tempat", style="dim")
            table.add_column("Lintang Tempat", style="dim")
            table.add_column("Bujur Tempat", style="dim")
            table.add_column("Ketinggian Tempat", style="dim")
            table.add_column("Time Zone", style="dim")

            for row in rows:
                table.add_row(
                    row[1],
                    str(row[2]),
                    str(row[3]),
                    str(row[4]),
                    str(row[5]),
                )
            console = Console()
            console.print(table, justify="center")
