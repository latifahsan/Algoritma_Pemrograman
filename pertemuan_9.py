# --- LIST ---

# kumpulan data numbers
data_angka = [1,5,2,3]
print(data_angka)

# kumpulan data string
data_string = ["ucup", "adit", "siti"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, True, False]
print(data_boolean)

# kumpulan data campuran
data_campuran = [1,"bakwan",2,"cireng","ucup",True,"adit",False]
print(data_campuran)

# cara alternatif
data_range = range(0,10,2) # Start Stop Step
print(data_range)
data_list = list(data_range)
print(data_list)

# list dengan for loop list comprehension
list_for = [i ** 2 for i in range(0,10)]
print(list_for)

# list dengan for dengan if
list_for_if = [i for i in range(0,10) if i !=5]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i %2 == 0]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i %2 != 0]
print(list_for_if)


# --- OPERASI LIST ---

# index 0(-3)   1(-2)   2(-1)
data = ["ucup","adit","dudung"]

# mengambil data dari list
data_0 = data[0]
print(f"data pertama(index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

# mengambil info jumlah data dalam list
panjangData = len(data)
print(f"panjang data adalah = {panjangData}")

# manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

# data.insert(posisi,item)
data.insert(1,"asep")
print(f"data sesudah ditambah = \n{data}")

# menambah di akhir list 
data.append("ririn")
print(f"data ditambah lagi = \n{data}")

# menambah list dengan list 
data_baru = ["luffy", "zoro", "nami"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data 
# kita ubah data 2 menjadi jarwo
data[2] = "jarwo"
print(f"data setelah di ubah = \n{data}")

# menghapus data 
data.remove("ucup")
print(f"data setelah di hapus = \n{data}")

# menghapus data paling belakang
data.pop()
print(f"data setelah di hapus paling belakang = \n{data}")




# --- OPERASI LIST ---

# index 0(-3) 1(-2) 2(-1)
data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]

print(f"data angka = \n {data_angka}")

# count data 
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"Jumlah angka 4 = {jumlah_data_4}")
print(f"Jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data 
data = ["rendi", "iqbal", "gana", "khairil"]

print(f"data = {data}")

index_iqbal = data.index("iqbal")
index_gana = data.index("gana")

print(f"index si iqbal = {index_iqbal}")
print(f"index si gana = {index_gana}")

# mengurutkan list 
print(f"data angka sebelum sort = \n {data_angka}")
data_angka.sort()
print(f"data angka setelah sort = \n {data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse
print(f"data direverse = \n {data_angka}")
print(f"data direverse = {data}")



# --- NESTED LIST ---
data_0 = [1,2]
data_1 = [3,4] 

data_list_biasa = [1,2,3,4]

print(f"list biasa = {data_list_biasa}")

list_2D= [data_0,data_1,6,7]
print(f"list 2D = {list_2D}")

# contoh penggunaan
peserta_0 = ["rendi", 25, "Laki-laki"]
peserta_1 = ["joni", 10, "Laki-laki"]
peserta_2 = ["eka", 50, "Wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t : {peserta_0}")
    print(f"umur\t : {peserta_1}")
    print(f"gender\t : {peserta_2}\n")