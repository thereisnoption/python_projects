#Program Python yang mengonversi suhu dari Fahrenheit ke Celsius

tempFahrenheit = float(input("Masukkan suhu dalam fahrenheit: "))
tempCelsius = (tempFahrenheit - 32) * (5/9)

print("Suhu dalam celsius:", tempCelsius)