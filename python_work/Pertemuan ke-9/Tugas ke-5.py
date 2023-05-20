"""
Program yang merekam stok, jumlah pembelian, dan sisa tiket dua film
dengan peringatan jika pembelian lebih besar dari stok tiket saat ini
"""

film1 = input("Masukkan judul Film 1: ")
film2 = input("Masukkan judul Film 2: ")

stok1 = int(input(f"\nMasukkan stok tiket Film 1: "))
stok2 = int(input(f"Masukkan stok tiket Film 2: "))

while True:
    pFilm = int(input(f"\nPilih judul film (1 atau 2): "))

    if pFilm == 1:
        pembelian = int(input(f"Masukkan jumlah pembelian tiket Film 1: "))

        if pembelian > stok1:
            print("Maaf, jumlah pembelian lebih banyak dari stok.")
            print(f"Jumlah tiket Film 1 saat ini: {stok1}")
        else:
            print("Terima kasih")

            stok1 -= pembelian
            print(f"Jumlah tiket Film 1 saat ini: {stok1}")
    elif pFilm == 2:
        pembelian = int(input(f"Masukkan jumlah pembelian tiket Film 2: "))

        if pembelian > stok2:
            print("Maaf, jumlah pembelian lebih banyak dari stok.")
            print(f"Jumlah tiket Film 2 saat ini: {stok2}")
        else:
            print("Terima kasih")

            stok2 -= pembelian
            print(f"Jumlah tiket Film 2 saat ini: {stok2}")

    if stok1 + stok2 <= 0:
        print(f"\nMaaf tiket sudah habis, silakan bisa coba nonton TV saja.")
        break