import datetime
import string
import random

perpus_template = {
    'judul':'judul',
    'penulis':'penulis',
    'tahun':0000,
    'pinjam':datetime.datetime(1111,1,11),
    'status':'status',
}

data_perpus = {}

while True:
    print()
    print(f"{'SELAMAT DATANG':^30}")
    print(f"{'DATA PERPUSTAKAAN':^30}")
    print("-"*30)
    perpus = dict.fromkeys(perpus_template.keys())
    perpus['judul'] = input("Judul Buku: ")
    perpus['penulis'] = input("Nama Penulis: ")
    perpus['tahun'] = int(input("Tahun Terbit (YYYY): "))
    TAHUN_PINJAM = int(input("Tahun Terakhir Pinjam (YYYY): "))
    BULAN_PINJAM = int(input("Bulan Terakhir Pinjam (1-12): "))
    TANGGAL_PINJAM = int(input("Tanggal Terakhir Pinjam (1-31): "))
    perpus['pinjam'] = datetime.datetime(TAHUN_PINJAM,BULAN_PINJAM,TANGGAL_PINJAM)
    perpus['status'] = input("Status Buku (Tersedia/Tidak)?: ")
    print()

    kode = ''.join((random.choice(string.ascii_uppercase) for i in range(3)))
    KEY = (perpus['penulis'],kode)
    data_perpus.update({KEY:perpus})
    
    print(f"{'KEYS':^25} | {'JUDUL BUKU':^25} | {'PENULIS':^20} | {'TAHUN TERBIT':^15} | {'TANGGAL TERAKHIR PINJAM ':^24} | {'STATUS':^8}")
    print('='*135)
    
    for perpus in data_perpus:
        KEY = perpus
        JUDUL_BUKU = data_perpus[KEY]['judul']
        PENULIS = data_perpus[KEY]['penulis']
        TAHUN_TERBIT = data_perpus[KEY]['tahun']
        PINJAM_TANGGAL = data_perpus[KEY]['pinjam'].strftime("%x")
        STATUS = data_perpus[KEY]['status']
        print(f"{str(KEY):<25} | {JUDUL_BUKU:<25} | {PENULIS:<20} | {TAHUN_TERBIT:^15} | {PINJAM_TANGGAL:^24} | {STATUS:<8}")
    
    print("\n")
    is_done = input("Mau tambah lagi (y/n)? ")
    if is_done == "n":
        break

print("\nAkhir dari program, terima kasih")