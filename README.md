# Aplikasi Data Astronomi Hilal Berbasis CLI Dengan Metode Skyfield

![Buid Status](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Aplikasi Data Astronomi ini ditujukan untuk memenuhi tugas akhir skripsi. Aplikasi ini bisa di jalankan lewat terminal dengan menggunakan perintah command line. 
## Fitur Aplikasi 

- Menyimpan Data Tempat 
- Mengetahui data Hilal setiap menitnya berupa ketinggian hilal, elongasi dan iluminasi 
- Mengeksport ke file PDF

## Teknologi Yang Digunakan

Aplikasi ini memiliki teknologi yang digunakan:

- [Skyfield](https://rhodesmill.org/skyfield/) - Untuk Melakukan Perhitungan data Astronomi Hilal
- [Pandas](https://pandas.pydata.org/) - Untuk Mengatur Data
- [Typer](https://typer.tiangolo.com/) - Untuk Menjalankan Perintah Aplikasi CLI 
- [Rich](https://rich.readthedocs.io/en/stable/introduction.html) - Untuk Mempercantik Tampilan Aplikasi

## Installation

Cara menginstall aplikasi ini diberbagai device dan sistem. Tetapi harus memastikan terlebih dahulu apakah python sudah terinstall atau belum dan pastikan versinya menggunakan python 3 keatas dengan cara:
```sh
python --version
```
Dan pastikan git sudah terinstall juga, dengan cara:
```sh
git --version
```
Berikutnya cara menginstall di berbagai device :
# Linux/Mac
Untuk menginstall dan menjalankan
```sh
mkdir data-astronomi
cd data-astronomi
git clone https://github.com/Sendyardy/data-astronomi-hilal.git
cd data-astronomi-hilal
source venv/bin/activate
pip install -r pakage.txt
python app/app.py --help
```

# Windows 
```sh
mkdir data-astronomi
cd data-astronomi
git clone https://github.com/Sendyardy/data-astronomi-hilal.git
cd data-astronomi-hilal
.\venv\bin\activate
pip install -r pakage.txt
python app\app.py --help
```







