import ephem


class Jamghurub:
    def get_sunset_time_ephem(
        self, latitude, longitude, altitude, tahun, bulan, tanggal
    ):
        observer = ephem.Observer()
        observer.lat = str(latitude)
        observer.lon = str(longitude)
        observer.elev = altitude
        observer.horizon = "-0:34"
        date = f"{tahun:04d}-{bulan:02d}-{tanggal:02d}"

        sun = ephem.Sun(observer)

        sunset_time = observer.next_setting(sun, start=ephem.Date(date))

        waktu_magrib = ephem.localtime(sunset_time)
        jam = int(waktu_magrib.hour)
        menit = int(waktu_magrib.minute)

        return jam, menit
