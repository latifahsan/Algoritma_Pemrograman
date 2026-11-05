print("\n==================== NOMOR 1 ====================")

kendaraan = ['motor', 'mobil', 'sepeda', 'bus']

# a. Tambahkan 'truk' di akhir list
kendaraan.append('truk')
print(f"a. data setelah ditambah = \n\t{kendaraan}")
# b. Sisipkan becak' pada index ke-1
kendaraan.insert(1,'becak')
print(f"b. data setelah disisipkan = \n\t{kendaraan}")
# c. Hapus data yang berada paling belakang dari list tersebut.
kendaraan.pop()
print(f"c. data setelah dihapus = \n\t{kendaraan}")
# d. Ubah elemen 'sepeda' menjadi 'skuter'.
kendaraan[3] = 'skuter'
print(f"d. data setelah diubah = \n\t{kendaraan}")
# e. Tampilkan informasi jumlah total data di dalam list tersebut
jumlah_data = len(kendaraan)
print(f"e. Jumlah data = \n\t{jumlah_data}")

print("=================================================\n")







print("==================== NOMOR 2 ====================")
angka = [75, 80, 90, 75, 85, 100, 65]

# a. Cari tahu di indeks ke berapa skor 100 berada.
index_100 = angka.index(100)
print(f"Skor 100 berada di index ke-{index_100}")
# b. Hitung ada berapa banyak siswa yang mendapatkan skor 75.
jumlah_75 = angka.count(75)
print(f"Skor 75 didapatkan oleh {jumlah_75} siswa")
# c. Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar.
angka.sort()
print(f"Urutan skor kecil ke besar = {angka}")
# d. Balikkan urutan list yang sudah diurutkan tersebut sehingga menjadi dari terbesar ke terkecil.
angka.reverse()
print(f"Urutan skor besar ke kecil = {angka}")

print("=================================================\n")







print("==================== NOMOR 3 ====================")
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]

# Gabungkan menu_tambahan ke dalam menu_utama menggunakan fungsi, kemudian tampilkan hasil dari data gabungan tersebut.
menu_utama.extend(menu_tambahan)
print(f"Hasil gabungan data = {menu_utama}")

print("=================================================\n")







print("==================== NOMOR 4 ====================")
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris",3000]]

# a. Tampilkan harga dari "Pensil" (yaitu 2000) dengan memanggil indeks baris dan kolom yang spesifik dari list tersebut.
pensil = data_barang[1]
harga_pensil = pensil[1]
print(f"Harga dari pensil yaitu {harga_pensil}\n")
# b. Gunakan perulangan untuk membaca data satu per satu, lalu tampilkan output dengan format: "Nama: [nama barang], Harga: [harga]" untuk setiap elemen di dalamnya.
for barang in data_barang:
    print(f"nama \t : {barang[0]}")
    print(f"harga \t : {barang[1]}\n")

print("=================================================")
