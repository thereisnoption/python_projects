#Soal nomor 1

mobilA = 200000
mobilB = 300000
mobilC = 400000
asuransi = 50000

jenisMobil = input("Masukkan jenis mobil yang disewa (A, B, atau C): ").lower()
jumlahHari = int(input("Masukkan jumlah hari sewa: "))

totalBiaya = 0

if jenisMobil == "a":
    totalBiaya = (asuransi + mobilA) * jumlahHari
elif jenisMobil == "b":
    totalBiaya = (asuransi + mobilB) * jumlahHari
elif jenisMobil == "c":
    totalBiaya = (asuransi + mobilC) * jumlahHari
else:
    print("Jenis mobil yang anda pilih tidak tersedia")

print("Total biaya sewa mobil adalah Rp", totalBiaya)