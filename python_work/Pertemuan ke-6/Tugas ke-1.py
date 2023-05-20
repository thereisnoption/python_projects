#Tugas ke-1

tempat = ("Rumah", "Perpusatakaan", "Pantai", "Gunung", "Bengkel")

print(tempat)
print(tempat[0])
print(tempat[1:4])
print(len(tempat))

tempat_baru = ("Kost", "Kampus", "Toko buku")

semua_tempat = tempat + tempat_baru

print(semua_tempat)
print(semua_tempat.count("Gunung"))
print(semua_tempat.index("Pantai"))