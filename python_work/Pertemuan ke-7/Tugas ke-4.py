#Program untuk mengecek apakah suatu bilangan bulat habis dibagi 2 dan/atau 3

bilangan = int(input("Masukkan bilangan bulat anda di sini: "))

modulo1 = bilangan % 2
modulo2 = bilangan % 3

if modulo1 == 0:
    print(f"{bilangan} habis dibagi 2")
    if modulo2 == 0:
        print(f"{bilangan} habis dibagi 3")
    else:
        print(f"{bilangan} tidak habis dibagi 3")
elif modulo1 != 0:
    print(f"{bilangan} tidak habis dibagi 2")
    if modulo2 == 0:
        print(f"{bilangan} habis dibagi 3")
    else:
        print(f"{bilangan} tidak habis dibagi 3")