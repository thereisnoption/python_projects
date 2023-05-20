#Program untuk mengecek apakah suatu bilangan merupakan bilangan ganjil atau genap

bilangan = int(input("Masukkan bilangan anda di sini: "))

if bilangan % 2 == 0:
    print(f"{bilangan} merupakan bilangan genap")
else:
    print(f"{bilangan} merupakan bilangan ganjil")