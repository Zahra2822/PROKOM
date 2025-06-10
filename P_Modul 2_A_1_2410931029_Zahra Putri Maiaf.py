#Program Pemesanan Tiket Pesawat
print ("Selamat datang di pemesanan tiket dari Padang")
Kota = str(input("Masukkan kota tujuan Anda = "))
if Kota == 'Medan' :
    HargaMedan = 1002600
elif Kota == 'Jakarta' :
    HargaJakarta = 2142900
elif Kota == 'Batam' :
    HargaBatam = 665400

PP = str(input("Apakah ingin memesan tiket Pulang Pergi?"))
if PP == 'Tidak' :
    if Kota == 'Medan' :
        print ("Harga tiket Anda = ", HargaMedan)
    if Kota == 'Jakarta' :
        print ("Harga tiket Anda = ", HargaJakarta)
    if Kota == 'Batam' :
        print ("Harga tiket Anda = ", HargaBatam)
elif PP == 'Ya' :
    if Kota == 'Medan' :
        HargaTotalM = HargaMedan*1.6
        print ("Harga tiket Anda = ", HargaTotalM)
    if Kota == 'Jakarta' :
        HargaTotalJ = HargaJakarta*1.6
        print ("Harga tiket Anda = ", HargaTotalJ)
    if Kota == 'Batam' :
        HargaTotalB = HargaBatam*1.6
        print ("Harga tiket Anda = ", HargaTotalB)
else :
    print ("Pilihan Anda tidak tersedia")