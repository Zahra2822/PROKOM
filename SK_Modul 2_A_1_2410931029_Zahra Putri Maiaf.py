user = 'zahraputrimaiaf'
pas = 2410931029 

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