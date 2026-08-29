### TUGAS PERTEMUAN 3
 
## NOMOR 1
nama = "Muhammad Latif Ahsan Jauhari" # nama dengan tipe data string
umur = 18                             # umur dengan tipe data integer
berat = 60.1                          # berat dengan tipe data float

print("Nama  :",nama)
print("Umur  :",umur,"tahun")
print("Berat :",berat,"Kg")


## NOMOR 2
angka_string = "123" 
angka_float = 45.67
angka_integer = 89

# 1. Konversi angka_string menjadi integer
konversi_1=int(angka_string)
print(konversi_1," | di samping tipe datanya :", type(konversi_1))

# 2. Konversi angka_float menjadi integer 
konversi_2=int(angka_float)
print(konversi_2,"  | di samping tipe datanya :", type(konversi_2))

# 3. Konversi angka_integer menjadi float
konversi_3=float(angka_integer)
print(konversi_3,"| di samping tipe datanya :", type(konversi_3))

# 4. Konversi angka_integer menjadi string
konversi_4=str(angka_integer)
print(konversi_4,"  | di samping tipe datanya :", type(konversi_4))




## NOMOR 3

# a. Meminta input usia (integer)
usia = int(input("Masukkan usia: "))
print("Usia =",usia,",type =",type(usia))

# b. Meminta input tinggi badan (float)
tinggiBadan = float(input("Masukkan tinggi badan: "))
print("Tinggi badan =",tinggiBadan,",type =",type(tinggiBadan))

# c. Meminta input nama (string)
nama = input("Masukkan nama: ")
print("Nama =",nama,",type =",type(nama))