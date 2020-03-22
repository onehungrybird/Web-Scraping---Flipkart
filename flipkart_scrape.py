from bs4 import BeautifulSoup
import requests
import re
import csv

csv_file = open('flipkart_iphone.csv','w',encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name','Rating','Price','Rating_Votes'])

source = requests.get('https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY').text
soup = BeautifulSoup(source,'lxml')
#print(soup.prettify())

for source in soup.find_all('div',class_ = '_3liAhj'):

	name =  source.find('a',class_ = '_2cLu-l')['title']
	print(name)

	try:
		rating = source.find('div',class_ = 'hGSR34').text
	except Exception as e:
		rating = None
	print(rating)
	
	# rating = source.find('div',class_ = 'hGSR34').text
	# print(rating)

	price = source.find('div',class_ = '_1vC4OE').text
	print(price)

	try:
		rating_votes = source.find('span',class_ = '_38sUEc').text
	except Exception as e:
		rating_votes = None
	print(rating_votes)
	
	# rating_votes = source.find('span',class_ = '_38sUEc').text
	# # rating_votes = re.sub('(',' ',rating_votes)
	# # rating_votes = re.sub(')',' ',rating_votes)
	# print(rating_votes)

	print()
	csv_writer.writerow([name,rating,price,rating_votes])

csv_file.close()