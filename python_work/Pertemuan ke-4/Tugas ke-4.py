#Program dengan masukan dua nilai boolean dan menampilkan hasil operasi logika

print("Masukkan B untuk nilai BENAR dan langsung enter untuk nilai SALAH")

data1 = bool(input("Masukkan nilai boolean pertama (B/Enter) "))
data2 = bool(input("Masukkan nilai boolean kedua (B/Enter) "))

dan = data1 and data2
atau = data1 or data2
bukan1 = not data1
bukan2 = not data2
bukanDan = not dan
bukanAtau = not atau

print("Nilai operasi logika AND antara", bool(data1), "dengan", bool(data2), "adalah", dan)
print("Nilai operasi logika OR antara", bool(data1), "dengan", bool(data2), "adalah", atau)
print("Nilai operasi logika NOT", bool(data1), "adalah", bukan1)
print("Nilai operasi logika NOT", bool(data2), "adalah", bukan2)
print("Nilai operasi logika NAND antara", bool(data1), "dengan", bool(data2), "adalah", bukanDan)
print("Nilai operasi logika NOR antara", bool(data1), "dengan", bool(data2), "adalah", bukanAtau)