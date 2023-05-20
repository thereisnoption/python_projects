#Program Python yang menghitung volume tabung

PI = 3.14

radius = float(input("Masukkan jari-jari alas tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))

luasAlas = PI * (radius ** 2)
volumeTabung = luasAlas * tinggi

print("Volume dari tabung adalah", volumeTabung, "satuan volume")