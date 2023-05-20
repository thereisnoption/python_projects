#Program untuk mencetak bilangan ganjil antara 1 s.d. masukan dari user

num = int(input("Masukkan bilangan positif di sini: "))

count = 1

while count <= num:
    if count % 2 != 0:
        print(count)

    count += 1