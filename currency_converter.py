import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.rba.gov.au/statistics/frequency/exchange-rates.html')

soup = BeautifulSoup(page.text, 'html.parser')

soup.find('tr', id="TWI_4pm").decompose()
soup.find('tr', id="SDR").decompose()

currency_list = soup.find(class_='table-linear table-numeric width100')

currencies = currency_list
currencies_list=[]
pricing_list=[]
for tag in currency_list.findAll(True,{'id':True}) :
    currencies_list.append(tag['id'])

currency_list_items = currency_list.find_all(class_='highlight')

for currency_list in currency_list_items:
    prices = currency_list.contents[0]
    pricing_list.append(prices)

final_list=list(zip(currencies_list, pricing_list))

#print(final_list)

userInput = input("Currency?")

for x in range(len(final_list)):
    print(x)
    #print(str(final_list[x+1][0]))
    if x == str(final_list[x][0]):
        print(str(final_list[x+1][1]))
        break
    else: 
        print(final_list[2][0])
        break