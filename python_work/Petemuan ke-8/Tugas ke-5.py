#Tugas ke-5

ukuranTabel = int(input("Masukkan ukuran tabel perkalian: ")) + 1

for i in range(1, ukuranTabel):
    for j in range(1, ukuranTabel):
        print(f"Hasil kali {i} dan {j} adalah {i * j}")
    
    print("")