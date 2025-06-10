print ("*** Program Login ***")
print ("Kesempatan login = 3")
username = 'zahramaiaf'
password = 2005
kesempatan = 0

for i in range (3) :
    while kesempatan < 3 :
        usr = str(input("Masukkan Username = "))
        pwd = int(input("Masukkan Password = "))

        if usr == username and pwd == password :
            print ("Selamat datang Zahra!")
            break
        else :
            kesempatan += 1 
            print("Username atau password salah. Kesempatan yang telah digunakan: ", kesempatan)
            continue
    if kesempatan == 3 :
        print("Kesempatan Anda habis. Login gagal. Silahkan kembali beberapa waktu lagi.")
        exit()

    else :
        while True :
            user = 'zahraputrimaiaf'
            pas = 2410931029 

            print ("*** Selamat Datang di Program Selanjutnya ***")
            username = str(input("Masukkan username anda = "))
            password = int(input("Masukkan password anda = "))

            if username == user and password == pas :
                print("Anda berhasil login")
            elif username != user and password != pas :
                print("Anda gagal login")
            elif username != user :
                print("Maaf username Anda salah")
            elif password != pas :
                print("Maaf password Anda salah")
            else :
                print("Pilihan Anda tidak tersedia!")

            TambahData = input("Apakah Anda ingin menambah data lagi? (Yes/No): ").lower()
            if TambahData != 'Yes':
                print("Terima kasih! Login Berhasil")
                break
            