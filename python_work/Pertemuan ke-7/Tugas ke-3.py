#Program untuk mengecek apakah sebuah karakter merupakn huruf vokal atau konsonan

hVokal = ["a", "i", "u", "e", "o"]

karakter = input("Masukkan satu karakter anda di sini: ")

if karakter.lower() in hVokal:
    print(f"{karakter} merupakan huruf vokal")
else:
    print(f"{karakter} merupakan huruf konsonan")