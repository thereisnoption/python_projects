"""
Program yang merekam stok, jumlah pembelian, dan sisa tiket sebuah film
dengan peringatan jika pembelian lebih besar dari stok tiket saat ini
"""

stok = int(input(f"Masukkan stok tiket film GoTG Vol. 3: "))

while stok > 0:
    pembelian = int(input(f"\nMasukkan jumlah pembelian tiket: "))

    if pembelian > stok:
        print("Maaf, jumlah pembelian lebih banyak dari stok.")
        print(f"Jumlah tiket saat ini: {stok}")
    else:
        print("Terima kasih")

        stok -= pembelian
        print(f"Jumlah tiket saat ini: {stok}")

    if stok == 0:
        print(f"\nMaaf tiket sudah habis, silakan bisa coba nonton Mario Bros.")