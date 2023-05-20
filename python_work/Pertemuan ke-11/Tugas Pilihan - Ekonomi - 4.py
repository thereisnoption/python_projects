rate = {
    "USD": 1,
    "EUR": 0.93,
    "JPY": 137.97,
    "GBP": 0.80,
    "AUD": 1.50,
    "SGD": 1.34,
    "IDR": 14936,
    "SAR": 3.75
}

def convert_currency(currency1, currency2, original_amount):
    if currency1 not in rate or currency2 not in rate:
        raise ValueError("Invalid currency")

    if currency1 == "USD":
        converted_amount = original_amount * rate[currency2]
    else:
        converted_amount = original_amount * rate[currency2] / rate[currency1]

    return converted_amount

print('''
Program konversi mata uang untuk mata uang di bawah ini:

United States Dollar (USD)
Euro (EUR)
Japanese Yen (JPY)
Great Britain Pound Sterling (GBP)
Australian Dollar (AUD)
Singapore Dollar (SGD)
Indonesian Rupiah (IDR)
Saudi Riyal (SAR)
''')

currency1 = input("Masukkan mata uang asal (USD dll.): ").upper()
currency2 = input("Masukkan mata uang tujuan (USD dll.): ").upper()

original_amount = float(input("\nMasukkan jumlah uang yang akan dikonversi: "))

try:
    converted_amount = convert_currency(currency1, currency2, original_amount)
    print(f"{original_amount} {currency1} = {converted_amount} {currency2}")
except ValueError:
    print("Invalid currency")