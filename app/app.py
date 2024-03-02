import typer
from myapp.view import viewcreat
from myapp.crud import Delete, read
from myapp.crud import select
from myapp.view import updatedata
from myapp.main import TanggalData, main, print, PrintTanggalData

app = typer.Typer()


@app.command()
def buat_tempat():
    """
    Untuk Membuat Dan Menambahkan Data Tempat Baru Ke Database
    Gunakan Comand: python3 app.py buat-tempat
    """
    view_tambah = viewcreat.ViewCreat()
    view_tambah.tambah_data()


@app.command()
def tampil_all_tempat():
    """
    Untuk Menampilkan Seluruh Data Tempat Yang Tersimpan
    Gunakan Comand: python3 app.py tampil-all-tempat
    """

    lihat_data = read.Read()
    lihat_data.lihat_tempat()


@app.command()
def cari_tempat(nama: str):
    """
    Untuk Mencari Data Tempat
    Gunakan Comand: python3 app.py cari-tempat "nama tempat"
    """
    select_data = select.Select()
    select_data.pilih_tempat(nama)


@app.command()
def update_tempat(nama_tempat: str):
    """
    Untuk Memperbaharui Data Tempat
    Gunakan Comand: python3 app.py update-tempat "nama tempat"
    """
    perbaharui_data = updatedata.UpdateData()
    perbaharui_data.update_data(nama_tempat)


@app.command()
def delete_tempat(nama_tempat: str):
    """
    Untuk Menghapus Data Tempat
    Gunakan Comand: python3 app.py delete-tempat "nama tempat"
    """
    hapus_data = Delete()
    hapus_data.hapus_tempat(nama_tempat)


@app.command()
def lihat_data_astronomi(
    nama: str,
    bulan: str,
    tahun: int,
    before: int = typer.Option(
        None, "-b", help="Sebelum berapa menit terbenam matahari(e.g., -b 30)"
    ),
    after: int = typer.Option(
        None, "-a", help="Sesudah berapa menit terbenam matahari(e.g., -a 31)"
    ),
):
    """
    Untuk Melihat Data Astronomi Hilal
    Gunakan Comand: python3 app.py lihat-data-astronomi "nama tempat" "bulan hijriah" tahun hijriah -b (sebelum berapa menit) -a sesudah berapa menit)
    """
    pilihan = main.TampilData()
    pilihan.pilih_main(nama, bulan, tahun, before, after)


@app.command()
def print_data_astronomi(
    nama: str,
    bulan: str,
    tahun: int,
    before: int = typer.Option(
        None, "-b", help="Sebelum berapa menit terbenam matahari(e.g., -b 30)"
    ),
    after: int = typer.Option(
        None, "-a", help="Sesudah berapa menit terbenam matahari(e.g., -a 31)"
    ),
):
    """
    Untuk Mencetak Data Astronomi Hilal ke Bentuk PDF
    Gunakan Comand: python3 app.py print-data-astronomi "nama tempat" "bulan hijriah" tahun hijriah -b (sebelum berapa menit) -a sesudah berapa menit)
    """

    cetak = print.PrintData()
    cetak.print_main(nama, bulan, tahun, before, after)


@app.command()
def lihat_tanggal(
    nama: str,
    tanggal: int,
    bulan: int,
    tahun: int,
    before: int = typer.Option(
        None, "-b", help="Sebelum berapa menit terbenam matahari(e.g., -b 30)"
    ),
    after: int = typer.Option(
        None, "-a", help="Sesudah berapa menit terbenam matahari(e.g., -a 31)"
    ),
):
    """
     Untuk Melihat Data Astronomi Hilal Pertanggal
    Gunakan Comand: python3 app.py lihat-tanggal "nama tempat" tanggal bulan tahun -b (sebelum berapa menit) -a sesudah berapa menit)
    """

    pertanggal = TanggalData()
    pertanggal.tangal_main(nama, tanggal, bulan, tahun, before, after)


@app.command()
def print_tanggal(
    nama: str,
    tanggal: int,
    bulan: int,
    tahun: int,
    before: int = typer.Option(
        None, "-b", help="Sebelum berapa menit terbenam matahari(e.g., -b 30)"
    ),
    after: int = typer.Option(
        None, "-a", help="Sesudah berapa menit terbenam matahari(e.g., -a 31)"
    ),
):
    """Untuk Mencetak Data Astronomi Hilal Pertanggal Masehi
    Gunakan Comand: python3 app.py lihat-tanggal "nama tempat" tanggal bulan tahun -b (sebelum berapa menit) -a sesudah berapa menit)
    """

    print_pertanggal = PrintTanggalData()
    print_pertanggal.print_tangal(nama, tanggal, bulan, tahun, before, after)


if __name__ == "__main__":
    app()
