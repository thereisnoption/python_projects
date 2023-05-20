#Tugas ke-2

kamus = {"rumah": "house", "sekolah": "school", "perpustakaan": "library",
         "taman": "park", "kantor": "office", "mobil": "car", "motor": "motorcycle"}

print(kamus)
print(kamus.get("rumah"))
print(kamus.keys())
print(kamus.values())

kamus["sepeda"] = "bicycle"
kamus.update(mobil = "carriage")
kamus.pop("motor")

print(kamus.items())
print(kamus.get("mobil"))
print(len(kamus))