#Program untuk menghitung hasil pembagian bulat dan sisa bagi dari dua bilangan yang dimasukkan oleh user

bilangan = float(input("Masukkan bilangan yang akan dibagi: "))
pembagi = float(input("Masukkan bilangan pembagi: "))

pembagianBulat = bilangan // pembagi
sisaBagi = bilangan % pembagi

print("Hasil bagi bulat dari kedua bilangan adalah", pembagianBulat)
print("Hasil sisa bagi dari kedua bilangan adalah", sisaBagi)