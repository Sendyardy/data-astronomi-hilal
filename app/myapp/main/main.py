from .pilih import Pilih
from ..core.jamghurub import Jamghurub
from ..core.conversidate import Konversi
from ..core.skyfield_data import DataCalculator
from rich.console import Console
from rich.table import Table


class TampilData:
    def __init__(self):
        self.jamghurub = Jamghurub()
        self.konversi = Konversi()
        self.dataastro = DataCalculator()
        self.console = Console()

    def pilih_main(
        self, nama_tempat: str, bulan: str, tahun: int, before: int, after: int
    ):
        pilih = Pilih()
        select_data = pilih.pilih_tempat(nama_tempat)

        _, nama_tempat, latitude, longitude, elevetion, timezone = select_data

        def konversi_bulan(nama_bulan: str):
            bulan_hijri = {
                "Muhharam": 1,
                "Safar": 2,
                "Rabiul Awal": 3,
                "Rabiul Akhir": 4,
                "Jumadil Ula": 5,
                "Jumadil Akhir": 6,
                "Rajab": 7,
                "Syaban": 8,
                "Ramadhan": 9,
                "Syawal": 10,
                "Zulkaidah": 11,
                "Zulhijah": 12,
            }
            konversiBulan = bulan_hijri.get(nama_bulan.strip(), None)
            return int(konversiBulan) if konversiBulan is not None else None

        hasil_konversi = konversi_bulan(bulan)
        bulan_hijriah = int(hasil_konversi)

        tahun_hijrih = tahun

        masehi_konversi = self.konversi.hijri_to_masehi(tahun_hijrih, bulan_hijriah)
        tanggal_masehi, namabulan_masehi, bulan_masehi, tahun_masehi = masehi_konversi

        jam, menit = self.jamghurub.get_sunset_time_ephem(
            latitude, longitude, elevetion, tahun_masehi, tanggal_masehi, bulan_masehi
        )

        data_astro = {
            "year": tahun_masehi,
            "month": bulan_masehi,
            "day": tanggal_masehi,
            "hours": jam,
            "minute": menit,
            "timezone_offset": timezone,
            "langitude": latitude,
            "longitude": longitude,
            "elevetion": elevetion,
            "beforeTime": before,
            "afterTime": after,
        }
        dataAsto_hilal = self.dataastro.generate_data(data_astro)
        self.console.print(
            f"[green]Data Astronomi Hilal Untuk {nama_tempat}[/green]", justify="center"
        )
        self.console.print(
            f"[yellow]Akhir Bulan Terjadi Pada Tanggal {tanggal_masehi}:{namabulan_masehi}:{tahun_masehi}[/yellow]",
            justify="center",
        )
        self.console.print(
            f"[green] Koordinat: {latitude} LS {longitude} BT {elevetion} meter {timezone} GMT[/green]",
            justify="center",
        )
        self.console.print(
            f"[red]Dan Terbenam Matahari Terjadi Pada Jam {jam}:{menit}[/red]",
            justify="center",
        )
        table = Table(
            title=f"Data Astronomi Untuk Akhir Bulan {bulan} {tahun_hijrih}",
            show_header=True,
            header_style="bold magenta",
        )
        for column in dataAsto_hilal.columns:
            table.add_column(column)

        for index, row in dataAsto_hilal.iterrows():
            table.add_row(*[str(value) for value in row])
        self.console.print(table, justify="center")
