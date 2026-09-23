# 1. Buat program yang menampilkan bilangan ganjil dan genap dari 1 sampai 50 menggunakan perulangan
print("\n===daftar semua bilangan ganjil dan genap dari 1 sampai 50===")
angka = 0
while angka < 50:
    angka += 1
    if angka % 2 == 0:
        print(f"{angka} <- angka ini bilangan genap")
    else:
        print(f"{angka} <- angka ini bilangan ganjil")
print("program selesai")





# 2. Buat program yang menampilkan semua bilangan prima antara 1 sampai 100 menggunakan perulangan
print("\n===daftar semua angka prima antara 1 sampai 100===")
for angka in range(2,101): 
    for i in range(2,angka):
        if angka % i == 0:
            break
    else :
        print(angka)
print("program selesai")


