#Program yang merekam stok, jumlah pembelian, dan sisa tiket sebuah film

stok = int(input(f"Masukkan stok tiket film GoTG Vol. 3: "))

while stok > 0:
    pembelian = int(input(f"\nMasukkan jumlah pembelian tiket: "))

    print("Terima kasih")

    stok -= pembelian
    print(f"Jumlah tiket saat ini: {stok}")