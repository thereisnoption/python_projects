#Tugas ke-3

string = input("Masukkan sebuah string: ")
karakter = input("Masukkan karakter yang ingin dihitung: ")

jumlah = []

for i in string:
    if i.lower() == karakter.lower():
        jumlah.append(i)

print(f"Jumlah karakter {karakter} dalam string adalah {len(jumlah)}")