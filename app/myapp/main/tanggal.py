from .pilih import Pilih
from ..core.jamghurub import Jamghurub
from ..core.skyfield_data import DataCalculator
from rich.console import Console
from rich.table import Table


class TanggalData:
    def __init__(self):
        self.jamghurub = Jamghurub()
        self.dataastro = DataCalculator()
        self.console = Console()

    def tangal_main(
        self,
        nama_tempat: str,
        tanggal: int,
        bulan: int,
        tahun: int,
        before: int,
        after: int,
    ):
        pilih = Pilih()
        select_data = pilih.pilih_tempat(nama_tempat)

        _, nama_tempat, latitude, longitude, elevetion, timezone = select_data

        jam, menit = self.jamghurub.get_sunset_time_ephem(
            latitude, longitude, elevetion, tahun, tanggal, bulan
        )

        data_astro = {
            "year": tahun,
            "month": bulan,
            "day": tanggal,
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
            f"[green] Koordinat: {latitude} LS {longitude} BT {elevetion} meter {timezone} GMT[/green]",
            justify="center",
        )
        self.console.print(
            f"[red]Dan Terbenam Matahari Terjadi Pada Jam {jam}:{menit}[/red]",
            justify="center",
        )
        table = Table(
            title=f"Data Astronomi Hilal Untuk Tanggal {tanggal}/{bulan}/{tahun}",
            show_header=True,
            header_style="bold magenta",
        )
        for column in dataAsto_hilal.columns:
            table.add_column(column)

        for index, row in dataAsto_hilal.iterrows():
            table.add_row(*[str(value) for value in row])
        self.console.print(table, justify="center")
