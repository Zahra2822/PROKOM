data_penyerang = [
    {"nama" : "Vinicius Junior", "umur" : "24", "durasi" : "3 tahun", "nilai" : "Rp 3.476,33 M"},
    {"nama" : "Rodrygo", "umur" : "24", "durasi" : "4 tahun", "nilai" : "Rp 1.738,16 M"},
    {"nama" : "Arda Guler", "umur" : "19", "durasi" : "5 tahun", "nilai" : "Rp 782,17 M"},
    {"nama" : "Brahim Diaz", "umur" : "25", "durasi" : "3 tahun", "nilai" : "Rp 608,36 M"},
    {"nama" : "Kylian Mbappe", "umur" : "26", "durasi" : "5 tahun", "nilai" : "Rp 2.781,06 M"}
    ]

while True :
    print ("Pilihan Data Penyerang Real Madrid FC")
    print ("1. Tampilkan Data Penyerang")
    print ("2. Menghapus Data Penyerang")
    print ("3. Menambah Data Penyerang")
    print ("4. Mengganti Data Penyerang")
    print ("5. Keluar")
    opsi = int(input("Masukkan pilihan : "))

    if opsi == 1 :
        print ("Data Penyerang Real Madrid FC")
        for data in data_penyerang :
            print (f"{data['nama']}, Umur : {data['umur']}, Durasi Kontrak : {data['durasi']}, Nilai Kontrak : {data['nilai']}")
        print ("*Note: Data dimulai dari nomor 1")
        
    elif opsi == 2 :
        for data in data_penyerang :
            print (f"{data['nama']}, Umur : {data['umur']}, Durasi Kontrak : {data['durasi']}, Nilai Kontrak : {data['nilai']}")
        print ("*Note: Data dimulai dari nomor 1")
        nomor = int(input("Masukkan nomor data penyerang yang ingin dihapus : ")) - 1
        if 0 <= nomor < len(data_penyerang) :
            data_penyerang.pop(nomor)
            print("Anda berhasil menghapus data")
        else :
            print ("Nomor tidak valid")
        
    elif opsi == 3 :
        baru1 = input("Masukkan nama penyerang : ")
        baru2 = int(input("Masukkan umur penyerang : "))
        baru3 = input("Masukkan durasi kontrak penyerang :  ")
        baru4 = input("Masukkan nilai kontrak penyerang : ")
        data_penyerang.append ({"nama" : baru1, "umur" : baru2, "durasi" : baru3, "nilai" : baru4})
        print ("Anda berhasil menambah data")

    elif opsi == 4 :
        for data in data_penyerang :
            print (f"{data['nama']}, Umur : {data['umur']}, Durasi Kontrak : {data['durasi']}, Nilai Kontrak : {data['nilai']}")
        print ("*Note: Data dimulai dari nomor 1")
        nomor = int(input("Masukkan nomor data penyerang yang ingin diubah : ")) - 1
        if 0 <= nomor < len(data_penyerang) :
            print ("Menu ubah data : ")
            print ("1. Nama penyerang")
            print ("2. Umur penyerang")
            print ("3. Durasi kontrak penyerang")
            print ("4. Nilai kontrak penyerang")
            print ("Pilih data yang ingin di ubah :")
            pilih = int(input("Masukkan nomor menu yang ingin diubah : "))
            if pilih == 1 :
                nama_baru = input ("Masukkan nama yang baru : ")
                data_penyerang[nomor]['nama'] = nama_baru
                print ("Anda berhasil mengganti data")
            elif pilih == 2 :
                umur_baru = input ("Masukkan umur yang baru : ")
                data_penyerang[nomor]['umur'] = umur_baru
                print ("Anda berhasil mengganti data")
            elif pilih == 3 :
                durasi_baru = input ("Masukkan durasi kontrak yang baru : ")
                data_penyerang[nomor]['durasi'] = durasi_baru
                print ("Anda berhasil mengganti data")
            elif pilih == 4 :
                nilai_baru = input ("Masukkan nilai kontrak yang baru : ")
                data_penyerang[nomor]['nilai'] = nilai_baru
                print ("Anda berhasil mengganti data")
            else : 
                print ("Nomor tidak valid")
        else :
            print ("Nomor tidak valid")

    elif opsi == 5 :
        print ("Terima kasih sudah menggunakan program ini")
        break
        
    else :
        print("Nomor tidak valid")
        break 

