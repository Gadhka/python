import re
import requests
class CurrencyConvert:
    def __init__(self):
        self.AllowedCurrency = ["USD","CAD","INR","EUR"]
        self.convert = lambda amount,From,to:f"https://api.frankfurter.app/latest?amount={amount}&from={From}&to={to}"
    def App(self):
        print("REAL API")
        print("make sure you are following the instraction! ")
        while True:
            print("\n".join([currency for currency in self.AllowedCurrency]))
            convertCurrency = input("Type '100 USD to EUR' like that: ").rstrip().upper()
            amount = re.search((r"\d+(\.\d+)?"),convertCurrency)
            FromCurrency = re.search(r"\b[a-zA-Z]{3}\b",convertCurrency)
            ToCurrency = re.search(r"\bTO (.+)",convertCurrency)
            if not FromCurrency[0]==ToCurrency[1] and len(convertCurrency.split(' ')) == 4 and amount.group(0) and FromCurrency[0] and ToCurrency[1]:
                url = self.convert(amount.group(0),FromCurrency[0],ToCurrency[1])
                self.Request(url,ToCurrency[1],amount=amount.group(0),fromcurrency=FromCurrency[0])
                do_you_wanto_calculate_currency = input("do you wanto calculate again (yes or no) ")
                if do_you_wanto_calculate_currency.lower() == "y" or do_you_wanto_calculate_currency =="yes":
                    continue
                else :
                    break
            else:
                break

    def Request(self,url,ToCurrency,amount,fromcurrency):
        request = requests.get(url=url)
        if request.status_code == 200: 
            response = request.json()
            print(f"{amount} {fromcurrency} TO {ToCurrency} == {response["rates"][ToCurrency]}")
        else:
            print("please check you internet! ")
            return False

if __name__=="__main__":
    CurrencyConvert().App()