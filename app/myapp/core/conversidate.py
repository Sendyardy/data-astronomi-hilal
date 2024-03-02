from hijri_converter import convert


class Konversi:
    def hijri_to_masehi(self, hijri_year, hijri_month):
        try:
            # Membuat objek Hijri dengan parameter tahun, bulan, dan hari
            tanggal_hijri = 29
            masehi_date = convert.Hijri(
                hijri_year, hijri_month, tanggal_hijri
            ).to_gregorian()

            tanggal_masehi = masehi_date.day
            nama_bulan_masehi = masehi_date.strftime("%B")
            tahun_masehi = masehi_date.year
            angka_bulan_masehi = masehi_date.month


            # Mengonversi tanggal Hijriah ke tanggal Masehi
            return tanggal_masehi, nama_bulan_masehi, angka_bulan_masehi, tahun_masehi
        except ValueError as e:
            print(f"Error: {e}")
            return e
