#Program untuk mengecek apakah suatu bilangan adalah bilangan positif, nol, atau negatif

bilangan = float(input("Masukkan bilangan anda di sini: "))

if bilangan > 0:
    print(f"{bilangan} merupakan bilangan positif")
elif bilangan == 0:
    print(f"{bilangan} merupakan bilangan nol")
else:
    print(f"{bilangan} merupakan bilangan negatif")