"""
Program untuk menghitung indeks prestasi semester (IPS) berdasarkan
nilai yang diperoleh dari beberapa mata kuliah.
"""

nilaiHuruf = {
    "A" : 4,
    "A-" : 3.75,
    "A/B" : 3.5,
    "B+" : 3.25,
    "B" : 3,
    "B-" : 2.75,
    "B/C" : 2.5,
    "C+" : 2.25,
    "C" : 2,
    "C-" : 1.75,
    "C/D" : 1.5,
    "D+" : 1.25,
    "D" : 1,
    "E" : 0
}

jumlahSKS, nilaiSKS, nilaiSKSWhole = 0, 0, 0

def fIPS(nilaiSKSWhole, jumlahSKS):
    IPS = nilaiSKSWhole / jumlahSKS
    return IPS

while True:
    jumlahMK = int(input(f"Masukkan jumlah mata kuliah pada semester ini: "))

    count = 1

    while count <= jumlahMK:
        nilaiMK = input(f"\nMasukkan nilai mata kuliah dalam huruf: ").upper()

        if nilaiMK in nilaiHuruf.keys():
            sksMK = int(input(f"Masukkan SKS mata kuliah: "))

            nilaiSKS = nilaiHuruf[nilaiMK] * sksMK
        else:
            print(f"\nMaaf nilai yang anda masukan tidak tersedia di daftar nilai kami.")
            break

        jumlahSKS += sksMK
        nilaiSKSWhole += nilaiSKS

        count += 1

    if count >= jumlahMK:
        print(f"\nIndeks Prestasi Sementara (IPS) = {fIPS(nilaiSKSWhole, jumlahSKS)}")
    else:
        print(f"\nTerima kasih sudah menggunakan program kami.")

    flag = input(f"\nApakah Anda ingin menggunakan program ini lagi (Y/T): ").upper()
    print("")

    if flag == "Y":
        continue
    else:
        break