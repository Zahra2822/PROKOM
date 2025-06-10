#Program Hitung Biaya Parkir

HargaParkirMotor = 2000
HargaParkirMobil = 5000

BanyakMotor = int(input("Banyak motor yang parkir ="))
BanyakMobil = int(input("Banyak mobil yang parkir ="))

TotalBiayaMotor = HargaParkirMotor*BanyakMotor
TotalBiayaMobil = HargaParkirMobil*BanyakMobil

TotalBiayaSeluruh = TotalBiayaMotor+TotalBiayaMobil

print("Total biaya keseluruhannya adalah = ", TotalBiayaSeluruh)
