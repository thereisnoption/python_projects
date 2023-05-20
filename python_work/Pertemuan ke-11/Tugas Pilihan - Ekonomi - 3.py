#Program untuk mengonversi nilai suatu mata uang ke mata uang yang lainnya

rate = {
    "USD" : 1,
    "EUR" : 0.93,
    "JPY" : 137.97,
    "GBP" : 0.80,
    "AUD" : 1.50,
    "SGD" : 1.34,
    "IDR" : 14936,
    "SAR" : 3.75
}

def USDto(currency, amount1):
    amount = amount1 * rate[currency]
    return amount

def C1toC2(currency1, currency2, amount1):
    amount = amount1 * (1 / rate[currency1]) * rate[currency2]
    return amount

print(
'''
Program konversi mata uang untuk mata uang di bawah ini:

United States Dollar (USD)
Euro (EUR)
Japanese Yen (JPY)
Great Britain Pound Sterling (GBP)
Australian Dollar (AUD)
Singapore Dollar (SGD)
Indonesian Rupiah (IDR)
Saudi Riyal (SAR)
'''
)

currency1 = input(f"Masukkan mata uang asal (USD dll.): ").upper()
currency2 = input(f"Masukkan mata uang tujuan (USD dll.): ").upper()

amount1 = float(input(f"\nMasukkan jumlah uang yang akan dikonversi: "))

if currency1 not in rate or currency2 not in rate:
    print("Mata uang yang Anda masukkan belum tersedia.")
else:
    if currency1 == "USD":
        amount2 = USDto(currency2, amount1)
        print(f"{amount1} USD = {amount2} {currency2}")
    else:
        amount2 = C1toC2(currency1, currency2, amount1)
        print(f"{amount1} {currency1} = {amount2} {currency2}")