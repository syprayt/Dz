import requests
from bs4 import BeautifulSoup

response = requests.get("https://bank.gov.ua/")
if response.status_code == 200:
    bs = BeautifulSoup(response.text, features="html.parser")
    list = bs.find_all("div", {"class":"value-full"})
    print(f"Курс Євро: {list[0].text}")
    print(f"Курс Долара: {list[1].text}")