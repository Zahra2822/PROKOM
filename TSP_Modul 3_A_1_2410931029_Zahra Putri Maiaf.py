#Program ATM

print ("=== Masukkan kartu ATM Anda pada mesin ===")
print ("=== Selamat datang Zahra Putri Maiaf ===")

pinATM = 931029
kesempatan = 0
awal = 2410931029


for kesempatan in range (3) :
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
        print ("Kesempatan Anda habis")
        break
    
    while True :
        print ("Saldo Anda saat ini Rp2.410.931.029")
        print ("Kode transaksi")
        print ("Tarik = 1, Transfer = 2, Setor Tunai = 3")
        pilihan = int(input("Anda ingin melakukan transaksi apa? ="))
        if pilihan == 1 :
            transaksi = float(input("Anda ingin menarik uang ="))
            if transaksi < awal :
                total = awal - transaksi 
                print ("Saldo Anda tersisa = ", total)
                awal -= transaksi
            elif transaksi > awal :
                print ("Saldo Anda tidak mencukupi")
                continue
        elif pilihan == 2 :
            transaksi = float(input("Anda ingin menstransfer uang ="))
            if transaksi < awal :
                total = awal - transaksi
                print ("Saldo Anda tersisa = ", total)
                awal -= transaksi
            elif transaksi > awal :
                print ("Saldo Anda tidak mencukupi")
                continue
        elif pilihan == 3 :
            transaksi = float(input("Anda ingin setor tunai ="))
            total = awal + transaksi
            print ("Total saldo Anda = ", total)
            awal += transaksi
        else :
            print ("Pilihan Anda tidak tersedia")
            continue

      
        lagi = str(input("Apakah Anda ingin melakukan transaksi lagi (ya/tidak)?")).lower()
        if lagi == 'ya' :
            continue
        else :
            print ("=== Selamat Anda telah berhasil melakukan transaksi ===")
            print ("Sisa saldo Anda ", total)
            exit ()
            