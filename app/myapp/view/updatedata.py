from rich.console import Console
from ..crud.update import Update
from ..crud.select import Select
import typer


class UpdateData:
    def __init__(self):
        self.console = Console()
        self.update = Update()
        self.selsec = Select()

    def convert_desimal(self, degrees, minutes, seconds):
        sign = -1 if degrees < 0 else 1
        decimal_value = abs(degrees) + (minutes / 60) + (seconds / 3600)
        return sign * decimal_value

    def input_user(self):
        self.console.print("[green]Rubah Data Tempat [/green]")
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

        ketinggian = float(self.console.input("[red]Ketinggian Tempat: [/red]"))

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

        return {
            "lintang_tempat": lintang_tempat,
            "bujur_tempat": bujur_tempat,
            "ketinggian": ketinggian,
            "time_zone": time_zone,
        }

    def update_data(self, nama_tempat: str):
        self.console.print(f"[green]Anda Akan Merubah Data {nama_tempat}[/green]")
        new_data = self.input_user()
        self.update.update_tempat(nama_tempat, new_data)
        self.console.print("[red]Data berhasil diperbaharui!!! [/red]")


if __name__ == "__main__":
    perbaharui_data = UpdateData()
    nama_tempat = typer.prompt("Enter Nama Tempat : ")
    perbaharui_data.update_data(nama_tempat)
