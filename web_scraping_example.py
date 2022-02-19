import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm


URL = "https://www.flipkart.com/search?q=smart+watches&sid=ajy%2Cbuh&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=smart+watches%7CSmart+Watches&requestId=086ce11f-a54f-4945-98ae-5e88d77898b1&as-backfill=on"
flipcart_request = requests.get(URL)

soup = BeautifulSoup(flipcart_request.content, 'html5lib')

all_mobile_info = []
row = soup.findAll('div' ,attrs={'class':'_1AtVbE col-12-12'})

for mobile in tqdm(row):
	mobile_info = {}
	name = mobile.find('div', attrs={'class': '_4rR01T'})
	price = mobile.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
	rating = mobile.find('div', attrs={'class': '_3LWZlK'})
	mobile_link = mobile.find('a', attrs={'class': '_1fQZEK'})

	if name:
		mobile_info['Mobile Name'] = name.text
	if price:
		mobile_info['Mobile Price'] = price.text
	if rating:
		mobile_info['Mobile Rating'] = rating.text
	if mobile_link:
		mobile_info['Mobile Link'] = mobile_link.href
	if mobile_info:
		all_mobile_info.append(mobile_info)


with open('mobile.csv', 'w', newline='') as f:
	w = csv.DictWriter(f,['Mobile Name','Mobile Price','Mobile Rating','Mobile Link'])
	w.writeheader()
	for mobile_data in all_mobile_info:
		w.writerow(mobile_data)
