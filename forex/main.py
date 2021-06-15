from forex_python.converter import CurrencyCodes, CurrencyRates
from forex_python.bitcoin import BtcConverter

currency = CurrencyCodes()

cur_symbol = currency.get_symbol("EUR")

cur_name = currency.get_currency_name("EUR")

if __name__ == "__main__":
    print(f"The currency name is: {cur_name}")
    print(f"The currency symbol is: {cur_symbol}")
