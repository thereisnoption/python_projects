#Debugging

umur = int(input("Masukkan umur Anda: ")) #harus dikonversikan ke bilangan
nilai = int(input("Masukkan nilai Anda: ")) #harus dikonversikan ke bilangan

if umur > 17: #umur di atas 17 tidak mengguakan tanda =, kurang tanda : di akhir baris
    if nilai >= 70:
        print("Selamat Anda lulus")
else:
    print("Maaf, Anda belum lulus")