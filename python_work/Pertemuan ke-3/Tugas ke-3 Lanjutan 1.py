#Program Python yang mengonversi suhu dari Fahrenheit ke Celsius, Réaumur, dan Kelvin

tempFahrenheit = float(input("Masukkan suhu dalam fahrenheit: "))
tempCelsius = (tempFahrenheit - 32) * (5/9)
tempReaumur = (tempFahrenheit - 32) * (4/9)
tempKelvin = (tempFahrenheit - 32) * (5/9) + 273.15

print("Suhu dalam celsius:", tempCelsius)
print("Suhu dalam reaumur:", tempReaumur)
print("Suhu dalam kelvin:", tempKelvin)