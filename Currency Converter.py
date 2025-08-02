def convert_currency(amount, from_currency, to_currency):
    rates = {
        'USD': 1.0,
        'INR': 83.10,
        'EUR': 0.91,
        'JPY': 142.25
    }

    if from_currency not in rates or to_currency not in rates:
        return "Unsupported currency"

    usd_amount = amount / rates[from_currency]
    converted = usd_amount * rates[to_currency]
    return round(converted, 2)

while True:
    from_cur = input("From (USD, INR, EUR, JPY): ").upper()
    to_cur = input("To (USD, INR, EUR, JPY): ").upper()
    try:
        amt = float(input("Amount: "))
        result = convert_currency(amt, from_cur, to_cur)
        print(f"{amt} {from_cur} = {result} {to_cur}")
    except ValueError:
        print("Invalid amount. Try again.")

    again = input("Convert again? (y/n): ").lower()
    if again != 'y':
        break
