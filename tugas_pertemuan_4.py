# Buatlah program yang meminta user memasukkan usia seseorang, lalu kategorikan usia tersebut berdasarkan kriteria berikut :
# 0-12 tahun : Anak-anak
# 13 - 17 : Remaja
# 18 - 59 tahun : Dewasa
# 60 tahun ke atas : lansia

usia = float(input("Masukkan usia anda : "))

if usia >=0 and usia <=12 :
    print("Anda adalah Anak-anak")
elif usia >=13 and usia <=17 :
    print("Anda adalah Remaja")
elif usia >=18 and usia <=59 :
    print("Anda adalah Dewasa")
elif usia >=60:
    print("Anda adalah lansia")
else :
    print("Usia anda tidak valid")