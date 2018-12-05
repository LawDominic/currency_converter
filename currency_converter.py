# import modules
import requests
from bs4 import BeautifulSoup

# get page to pull from
page = requests.get('https://www.rba.gov.au/statistics/frequency/exchange-rates.html')

# initialise BeautifulSoup to parse data 
parse = BeautifulSoup(page.text, 'html.parser')

# remove the following data from output 
parse.find('tr', id="TWI_4pm").decompose()
parse.find('tr', id="SDR").decompose()

# grabs data of interest
currency_list = parse.find(class_='table-linear table-numeric width100')

# setup lists
currencies_list=[]
rate_list=[]

# load currency code into list
for tag in currency_list.findAll(True,{'id':True}) :
    currencies_list.append(tag['id'])

# pull data with the 'highlight' class
currency_list_items = currency_list.find_all(class_='highlight')

# load currency rates into list
for currency_list in currency_list_items:
    rate = currency_list.contents[0]
    rate_list.append(rate)

# combine the two lists into a 2d array
final_list=list(zip(currencies_list, rate_list))

# function to convert the amount
def calculateOutput(userInput, amount): 
    if userInput == final_list[0][0]:
        converted_amount = amount*float(final_list[0][1])
        print("" + str(converted_amount) + " " + final_list[0][0])
    elif userInput == final_list[1][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
    elif userInput == final_list[2][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[2][0])
    elif userInput == final_list[3][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
    elif userInput == final_list[4][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
    elif userInput == final_list[5][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
    elif userInput == final_list[6][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
    elif userInput == final_list[7][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
    elif userInput == final_list[8][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
    elif userInput == final_list[9][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
    elif userInput == final_list[10][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
    elif userInput == final_list[11][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
    elif userInput == final_list[12][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
    elif userInput == final_list[13][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
    elif userInput == final_list[14][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
    elif userInput == final_list[15][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
    elif userInput == final_list[16][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
    elif userInput == final_list[17][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
    elif userInput == final_list[18][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])
    elif userInput == final_list[19][0]:
        converted_amount = amount*float(final_list[1][1])
        print("" + str(converted_amount) + " " + final_list[1][0])

# calls the calculateOutput function with the necessary commands
calculateOutput(input("Currency: ").upper(), float(input("Amount: ")))