#Program untuk mengonversi nilai suatu mata uang ke mata uang yang lainnya

IDR = {
    "USD" : 0.000067,
    "EUR" : 0.000062,
    "JPY" : 0.0092,
    "GBP" : 0.000054,
    "AUD" : 0.00010
}

USD = {
    "EUR" : 0.92,
    "JPY" : 136.50,
    "GBP" : 0.80,
    "AUD" : 1.50,
    "IDR" : 14868.90
}

EUR = {
    "JPY" : 148.39,
    "GBP" : 0.87,
    "AUD" : 1.63,
    "IDR" : 16158.78,
    "USD" :1.09
}

JPY = {
    "GBP" : 0.0059,
    "AUD" : 0.011,
    "IDR" : 108.96,
    "USD" : 0.0073,
    "EUR" : 0.0073
}

GBP = {
    "AUD" : 1.87,
    "IDR" : 18568.24,
    "USD" : 1.25,
    "EUR" : 1.15,
    "JPY" : 170.41
}

AUD = {
    "IDR" : 9905.99,
    "USD" : 0.67,
    "EUR" : 0.61,
    "JPY" : 90.90,
    "GBP" : 0.53
}

Currency = [IDR, USD, EUR, JPY, GBP, AUD]

print(
'''
Program konversi mata uang.

United States Dollar (USD)
Euro (EUR)
Japanese Yen (JPY)
Great Britain Pound Sterling (GBP)
Australian Dollar (AUD)
Indonesian Rupiah (IDR)
'''
)

currency1 = input(f"Masukkan mata uang asal (USD dll.): ").upper()
currency2 = input(f"Masukkan mata uang tujuan (USD dll.): ").upper()

amount1 = float(input(f"\nMasukkan jumlah uang yang akan dikonversi: "))
amount3 = 0

"""
def c1toc2(c1, c2, amount1):
    global amount3
    for i in Currency:
        if i == c1:
            print(i)
            for j in c1:
                print(j)
                if j == c2:
                    amount3 = amount1 * i[j]
    return amount3

amount2 = c1toc2(currency1, currency2, amount1)
print(amount2)
"""

for i in Currency:
    print(i)
    if i == currency1:
        print(i)
        for j in currency1.keys():
            print(j)
            if j == currency2:
                amount3 = amount1 * i[j]
                print(amount3)