#Tugas ke-4

jumlahBarang = int(input("Masukkan jumlah barang: ")) + 1

hargaBarang = []

for i in range(1, jumlahBarang):
    hBarang = int(input(f"Masukkan harga barang {i}: "))
    hargaBarang.append(hBarang)

print(f"Total belanjaan Anda adalah {sum(hargaBarang)}")