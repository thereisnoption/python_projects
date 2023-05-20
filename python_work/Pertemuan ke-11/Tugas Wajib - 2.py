"""
Program untuk menghitung indeks prestasi semester (IPS) berdasarkan
nilai yang diperoleh dari beberapa mata kuliah.
"""

nilaiHuruf = {
    "A" : 4,
    "A-" : 3.75,
    "A/B" : 3.5,
    "B+" : 3.25,
    "B" : 3,
    "B-" : 2.75,
    "B/C" : 2.5,
    "C+" : 2.25,
    "C" : 2,
    "C-" : 1.75,
    "C/D" : 1.5,
    "D+" : 1.25,
    "D" : 1,
    "E" : 0
}

def calculate_ips(courses):
    total_credit_hours = 0
    cumulative_weighted_grade_points = 0

    for course in courses:
        grade = get_grade(course)
        if grade is None:
            print("\nMaaf, nilai yang Anda masukkan tidak tersedia di daftar nilai kami.")
            continue

        credit_hours = get_credit_hours(course)
        weighted_grade_points = grade * credit_hours

        total_credit_hours += credit_hours
        cumulative_weighted_grade_points += weighted_grade_points

    if total_credit_hours > 0:
        ips = cumulative_weighted_grade_points / total_credit_hours
        return ips
    else:
        return None

def get_grade(course):
    grade = input(f"\nMasukkan nilai mata kuliah {course} dalam huruf: ").upper()
    return nilaiHuruf.get(grade)

def get_credit_hours(course):
    credit_hours = int(input(f"Masukkan SKS mata kuliah {course}: "))
    return credit_hours

while True:
    jumlah_mk = int(input(f"Masukkan jumlah mata kuliah pada semester ini: "))

    if jumlah_mk <= 0:
        print("Maaf, jumlah mata kuliah harus lebih besar dari 0.")
        continue

    courses = [f"ke-{i+1}" for i in range(jumlah_mk)]

    ips = calculate_ips(courses)

    if ips is not None:
        print(f"\nIndeks Prestasi Sementara (IPS) = {ips}")
    else:
        print("\nTidak ada mata kuliah yang dihitung.")

    flag = input(f"\nApakah Anda ingin menggunakan program ini lagi (Y/T): ").upper()
    print("")

    if flag != "Y":
        break