#Program Python yang mengonversi suhu dari Fahrenheit ke Celsius

print("Program untuk mengonversi suhu dari Fahrenheit ke Celsius")
print("Pilih C untuk konversi dari Celsius ke Fahrenheit")
print("Pilih F untuk konversi dari Fahrenheit ke Celsius")

flag = "Y"

while flag == "Y":
    
    promptRaw1 = input("Masukkan pilihan anda di sini: ")

    prompt1 = promptRaw1.upper()

    def f2c(tempFahrenheit):
        tempFahrenheit = float(tempFahrenheit)

        tempCelsius = (tempFahrenheit - 32) * (5/9)
        print("Suhu dalam celsius:", tempCelsius)

    def c2f(tempCelsius):
        tempCelsius = float(tempCelsius)

        tempFahrenheit = (tempCelsius * (9/5)) + 32
        print("Suhu dalam fahrenheit:", tempFahrenheit)

    if prompt1 == "C":
        tempCelsius = float(input("Masukkan suhu dalam celsius: "))

        c2f(tempCelsius)
    elif prompt1 == "F":
        tempFahrenheit = float(input("Masukkan suhu dalam fahrenheit: "))

        f2c(tempFahrenheit)
    else:
        print("Program tidak bisa melakukan operasi tersebut")


    flagRaw = input("Apakah anda ingin melakukan pengkonversian lagi? (Y/T) ")
    if flagRaw.upper == "Y":
        flag = "Y"
    elif flagRaw.upper() == "T":
        flag = "T"
    else:
        print("Masukkan tidak tersedia")

else:
    print("Terima kasih!")