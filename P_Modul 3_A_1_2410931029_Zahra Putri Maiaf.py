#Program ATM

print ("=== Masukkan kartu ATM Anda pada mesin ===")
print ("=== Selamat datang Zahra Putri Maiaf ===")

pinATM = 931029
kesempatan = 0


for kesempatan in range (1) :
    while kesempatan < 3 :
        pin = int(input("Masukkan pin ATM = "))
        if pin == pinATM :
            print ("Pin Anda benar!")
            break
        else :
            kesempatan += 1
            print ("Pin Anda salah, kesempatan yang telah Anda pakai =", kesempatan)
        continue
    else :
        kesempatan == 3
        print ("Kesempatan Anda habis, ulangi beberapa saat lagi")
        break
    
    while True :
        awal = 2410931029
        print ("Kode transaksi")
        print ("Tarik = 1, Transfer = 2, Setor Tunai = 3")
        pilihan = int(input("Anda ingin melakukan transaksi apa? ="))
        if pilihan == 1 :
            tarik = int(input("Anda ingin menarik uang ="))
            total1 = awal - tarik 
            print ("Saldo Anda tersisa = ", total1)
        elif pilihan == 2 :
            transfer = int(input("Anda ingin menstransfer uang ="))
            total2 = awal - transfer
            print ("Saldo Anda tersisa = ", total2)
        elif pilihan == 3 :
            setor = int(input("Anda ingin setor tunai ="))
            total3 = awal + setor
            print ("Saldo Anda sebanyak = ", total3)
        else :
            print ("Pilihan Anda tidak tersedia")

        lagi = str(input("Apakah Anda ingin melakukan transaksi lagi?"))
        if lagi != 'ya' :
            print ("=== Selamat Anda telah berhasil melakukan transaksi ===")
            print ("Nama pengguna Zahra Putri Maiaf")
            print ("Saldo awal anda = ", awal)
            print ("Jenis transaksi yang digunakan ", pilihan)
            break



    
    
