"""
Program yang menerima dua string sebagai input, yaitu sebuah kata dan sebuah karakter,
tujuannya adalah untuk menampilkan apakah kata tersebut mengandung karakter tersebut
"""

kata = input("Masukkan kata di sini: ").lower()
karakter = input("Masukkan karakter di sini: ").lower()

nilai = karakter in kata

print(f"Karakter {karakter.upper()!r} terkandung dalam kata {kata.capitalize()!r} bernilai {nilai}")