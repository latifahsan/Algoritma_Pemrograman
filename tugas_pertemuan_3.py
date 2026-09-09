# Tugas pertemuan 3

# diberikan sebuah bangunan dengan nilai berikut:
panjang = 12
lebar = 5
tinggi = 8

# a. hitunglah luas, volume, dan keliling dari bangunan tersebut!
# luas
print("\n======================= LUAS BANGUNAN =======================")
luas = 2 * (panjang*lebar+panjang*tinggi+lebar*tinggi)
print('luas =',2,'* (',panjang,'*',lebar,'+',panjang,'*',tinggi,'+',lebar,'*',tinggi,') =',luas)

# volume
print("\n====================== VOLUME BANGUNAN ======================")
volume = panjang * lebar * tinggi
print('volume =',panjang,'*',lebar,'*',tinggi,'=',volume)


# keliling
print("\n===================== KELILING BANGUNAN =====================")
keliling = 4 * (panjang + lebar + tinggi)
print('keliling =',4,'* (',panjang,'+',lebar,'+',tinggi,') =',keliling)

# b. apakah luas bangunan tersebut lebih luas dari 50?
print("\n================= APAKAH LUAS LEBIH DARI 50 =================")
hasil = luas > 50
print(luas,'>',50,'=',hasil)
print("hasilnya true, karena luasnya 392 yang bernilai lebih dari 50")

# c. apakah volume tersebut bernilai 480?
print("\n=============== APAKAH VOLUMENYA BERNILAI 480 ===============")
hasil = volume == 480
print(volume,'==',480,'=',hasil)
print("hasilnya true, karena volumenya sesuai/sama yaitu bernilai 480")