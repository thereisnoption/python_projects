#Program Python yang menghitung rata-rata, maksimum, dan minimum dari tiga bilangan

num1 = float(input("Masukkan bilangan pertama: "))
num2 = float(input("Masukkan bilangan kedua: "))
num3 = float(input("Masukkan bilangan ketiga: "))

bilangan = (num1, num2, num3)

total = sum(bilangan)
mean = total / 3
maks = max(bilangan)
minimum = min(bilangan)

print("Rata-rata:", mean)
print("Nilai maksimum:", maks)
print("Nilai minimum:", minimum)
print("Nilai total ketiga bilangan:", total)