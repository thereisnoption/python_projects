#Program untuk mengonversi nilai suatu mata uang ke mata uang yang lainnya

IDRto = {
    "USD" : 0.000067,
    "EUR" : 0.000062,
    "JPY" : 0.0092,
    "GBP" : 0.000054,
    "AUD" : 0.00010
}

USDto = {
    "EUR" : 0.92,
    "JPY" : 136.50,
    "GBP" : 0.80,
    "AUD" : 1.50
}

EURto = {
    "JPY" : 148.39,
    "GBP" : 0.87,
    "AUD" : 1.63
}

JPYto = {
    "GBP" : 0.0059,
    "AUD" : 0.011
}

GBPto = {
    "AUD" : 1.87
}

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
amount2 = 0

def c1toc2(c1, c2, amount1):
    if c1 == "IDR":
        if c2 == "IDR":
            return c1
        elif c2 == "USD":
            amount3 = amount1 * IDRto["USD"]
        elif c2 == "EUR":
            amount3 = amount1 * IDRto["EUR"]
        elif c2 == "JPY":
            amount3 = amount1 * IDRto["JPY"]
        elif c2 == "GBP":
            amount3 = amount1 * IDRto["GBP"]
        elif c2 == "AUD":
            amount3 = amount1 * IDRto["AUD"]
        else:
            print("error")
    elif c1 == "USD":
        if c2 == "USD":
            return c1
        elif c2 == "EUR":
            amount3 = amount1 * USDto["EUR"]
        elif c2 == "JPY":
            amount3 = amount1 * USDto["JPY"]
        elif c2 == "GBP":
            amount3 = amount1 * USDto["JPY"]
        elif c2 == "AUD":
            amount3 == amount1 * USDto["AUD"]
        elif c2 == "IDR":
            amount3 = amount1 * (1/IDRto["USD"])

    return amount3

amount2 = c1toc2(currency1, currency2, amount1)
print(amount2)