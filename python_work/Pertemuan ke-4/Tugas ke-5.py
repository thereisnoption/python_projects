"""
Program yang menerima 5 input nama buah, tujuannya adalah untuk
memeriksa apakah nama buah ke-6 yang dimasukkan ada di dalam list
"""

buah1 = input("Masukkan nama buah pertama: ").capitalize()
buah2 = input("Masukkan nama buah kedua: ").capitalize()
buah3 = input("Masukkan nama buah ketiga: ").capitalize()
buah4 = input("Masukkan nama buah keempat: ").capitalize()
buah5 = input("Masukkan nama buah kelima: ").capitalize()

buah = [buah1, buah2, buah3, buah4, buah5]

buah6 = input("Masukkan nama buah keenam: ").capitalize()

print(buah6, "ada di dalam list buah bernilai", buah6 in buah)
print(buah)