#Soal nomor 2

pSistolik = int(input("Masukkan nilai tekanan darah sistolik: "))
pDiastolik = int(input("Masukkan nilai tekanan darah diastolik: "))

kategori = ""

if pSistolik > 180 and pDiastolik > 120:
    kategori = "Hipertensi kritis"
elif pSistolik >= 160 and pDiastolik >= 100:
    kategori = "Hipertensi tingkat 2"
elif pSistolik >= 140 and pDiastolik >= 90:
    kategori = "Hipertensi tingkat 1"
elif pSistolik >= 120 and pDiastolik >= 80:
    kategori = "Prahipertensi"
elif pSistolik < 120 and pDiastolik < 80:
    kategori = "Normal"

print(f"Kategori tekanan darah {pSistolik}/{pDiastolik} mmHg adalah {kategori}")