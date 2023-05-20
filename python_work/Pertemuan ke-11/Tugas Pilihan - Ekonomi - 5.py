import requests

API_KEY = "glDZEnVyniQsTlFeH0LJwTskhetvRxxhryfdDkJ3"
API_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

def get_exchange_rates():
    response = requests.get(API_URL)
    data = response.json()
    if "data" in data:
        return data["data"]
    else:
        print("Failed to fetch exchange rates.")
        return {}

def convert_currency(amount, from_currency, to_currency):
    exchange_rates = get_exchange_rates()
    if from_currency in exchange_rates and to_currency in exchange_rates:
        rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        converted_amount = amount * rate
        return converted_amount
    else:
        print("Invalid currency.")
        return None


while True:
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the currency to convert from: ").upper()
    to_currency = input("Enter the currency to convert to: ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount is not None:
        print(f"{amount} {from_currency} = {converted_amount} {to_currency}")

    flag = input(f"\nDo you want to use this program again? (Y/N): ").upper()

    if flag != "Y":
        break