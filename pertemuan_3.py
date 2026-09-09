# ======================================3.1 aritmatika sederhana=======================================
# Operasi aritmatika

a = 10
b = 3

# Operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)

# Operasi kurang -
hasil = a - b
print(a,'-',b,'=',hasil)

# Operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# Operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

# Operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

# Operasi modulus %
hasil = a % b
print(a,'%',b,'=',hasil)

# Operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)


# =======================================3.2 Konversi celcius ke satuan lain==========================================

# latihan konversi temperature

print("\nPROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input('Masukkan suhu dalam celcius :'))
print("Suhu adalah ",celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah",reamur,"Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah",fahrenheit,"Fahrenheit")

# kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah",kelvin,"Kelvin")


# ================================================3.3 Operasi komperasi===================================

# setiap hasil dari operasi komperasi adalah boolean

# >,<,>=,<=,==,!=,is, is not 

a = 4
b = 2

# lebih besar dari >
print("========== lebih besar dari (>)")
hasil = a > b
print(a,'>',b,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# kurang dari  <
print("========== kurang dari (<)")
hasil = a < b
print(a,'<',b,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# lebih dari sama dengan >=
print("========== lebih dari sama dengan (>=)")
hasil = a >= b
print(a,'>=',b,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# kurang dari sama dengan <=
print("========== kurang dari sama dengan (<=)")
hasil = a <= b
print(a,'<=',b,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# sama dengan ==
print("========== sama dengan (==)")
hasil = a == b
print(a,'==',b,'=',hasil)
hasil = b == 3
print(b,'==',3,'=',hasil)
hasil = b == 2
print(b,'==',2,'=',hasil)

# tidak sama dengan !=
print("========== sama dengan (!=)")
hasil = a != b
print(a,'!=',b,'=',hasil)
hasil = b != 3
print(b,'!=',3,'=',hasil)
hasil = b != 2
print(b,'!=',2,'=',hasil)

# 'is' sebagai komparasi obj identity (bukan literal)
x = 5 # ini adalah assignment membuat object
y = 5
hasil = x is y
print('x is y =', hasil)

# 'is not' sebagai komparasi obj identity (bukan literal)
x = 5 # ini adalah assignment membuat object
y = 6
hasil = x is not y
print('x is not y =', hasil)