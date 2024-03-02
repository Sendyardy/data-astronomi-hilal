from rich.console import Console
from ..crud.creat import Create
from ..database.database import Database


class ViewCreat:
    def __init__(self):
        self.console = Console()
        self.creat = Create()

    def convert_desimal(self, degrees, minutes, seconds):
        sign = -1 if degrees < 0 else 1
        decimal_value = abs(degrees) + (minutes / 60) + (seconds / 3600)
        return sign * decimal_value

    def tambah_data(self):
        nama_tempat = self.console.input("[red]Masukan Nama Tempat : [/red]")
        self.console.print("[red]Masukan Lintang Tempat[/red]")

        def lintang():
            derajat = float(input("Derajat: "))
            menit = float(input("Menit: "))
            detik = float(input("Detik: "))
            return self.convert_desimal(derajat, menit, detik)

        lintang_tempat = lintang()
        self.console.print("[red]Masukan Bujur Tempat[/red]")

        def bujur():
            derajat = float(input("Derajat: "))
            menit = float(input("Menit: "))
            detik = float(input("Detik: "))
            return self.convert_desimal(derajat, menit, detik)

        bujur_tempat = bujur()

        ketinggiaan = float(self.console.input("[red]Ketinggian Tempat: [/red]"))

        def timezone():
            self.console.print("[green]====== TIME ZONE ======[/green]")
            self.console.print("[green]1. WIB - UTC+7[/green]")
            self.console.print("[green]2. WITA - UTC+8[/green]")
            self.console.print("[green]3. WIT - UTC+9[/green]")

            pilihan = input("Masukkan  Opsi \t: ")

            if pilihan == "1":
                return 7
            elif pilihan == "2":
                return 8
            elif pilihan == "3":
                return 9
            else:
                self.console.print(
                    "[yellow]Pilihan tidak valid. Silakan pilih 1, 2, atau 3.[/yellow]"
                )

        time_zone = timezone()

        if (
            not nama_tempat
            or not lintang_tempat
            or not bujur_tempat
            or not ketinggiaan
            or not time_zone
        ):
            self.console.print("[yellow]Data Harus Di Isi[/yellow]")
        else:
            data = Database()
            data.creat_table()
            self.creat.tambah_tempat(
                nama_tempat, lintang_tempat, bujur_tempat, ketinggiaan, time_zone
            )
