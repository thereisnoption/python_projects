#Program yang meminta dua masukan bilangan bulat untuk dibandingkan

num1 = int(input("Masukkan bilangan bulat pertama: "))
num2 = int(input("Masukkan bilangan bulat kedua: "))

sama = num1 == num2
tidakSama = num1 != num2
lebihBesar = num1 > num2
lebihKecil = num1 < num2
lebihBesarSama = num1 >= num2
lebihKecilSama = num1 <= num2

print(f"{sama}\n{tidakSama}\n{lebihKecil}\n{lebihBesarSama}\n{lebihKecilSama}")