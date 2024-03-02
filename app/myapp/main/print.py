from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from .pilih import Pilih
from ..core.jamghurub import Jamghurub
from ..core.conversidate import Konversi
from ..core.skyfield_data import DataCalculator
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from rich.console import Console
from rich.prompt import Prompt
import os


class PrintData:
    def __init__(self):
        self.jamghurub = Jamghurub()
        self.konversi = Konversi()
        self.dataastro = DataCalculator()
        self.console = Console()

    def print_main(
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

        filename = Prompt.ask("Masukan Nama File PDF : ", default="output")
        directory = Prompt.ask(
            "Tentukan Folder/Direktori Yang Dinginkan :", default="./"
        )

        if not os.path.exists(directory):
            self.console.print(
                "[bold red] ALERT :[/bold red] Folder/Direktory Tidak Ditemukan atau Belum Ada !!!"
            )
            exit()

        file_path = os.path.join(directory, filename + ".pdf")

        pdf = SimpleDocTemplate(file_path, pagesize=letter)

        table_data = [dataAsto_hilal.columns.tolist()] + dataAsto_hilal.values.tolist()
        table = Table(table_data)

        style = TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), (0.8, 0.8, 0.8)),
                ("TEXTCOLOR", (0, 0), (-1, 0), (1, 1, 1)),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                ("BACKGROUND", (0, 1), (-1, -1), (0.85, 0.85, 0.85)),
                ("GRID", (0, 0), (-1, -1), 1, (0.2, 0.2, 0.2)),
            ]
        )

        table.setStyle(style)

        title_style = ParagraphStyle(
            name="Title", fontName="Helvetica-Bold", fontSize=12, alignment=1
        )
        title = Paragraph(
            f"<b> Data Astronomi Hilal {nama_tempat} Untuk Tanggal {tanggal_masehi} {namabulan_masehi} {tahun_masehi}</b>",
            title_style,
        )
        deskripsi_text = f"Koordinat : {nama_tempat}  {latitude} Derajat LS {longitude} Derajat BT {elevetion} meter {timezone} GMT"
        deskripsi_style = ParagraphStyle(name='Explanation', fontName= 'Helvetica', fontSize=12, alignment=1 )
        deskripsi = Paragraph(deskripsi_text, deskripsi_style)
        spacer = Spacer(1, 20)
        tulisan = [title, deskripsi, spacer, table]

        pdf.build(tulisan)

        self.console.print(
            f"Data Telah di cetak dalam bentuk PDF dengan Nama File [bold cyan]{filename}.pdf[/bold cyan] di Folder/Direktory [bold cyan]{directory}[/bold cyan]."
        )
