from bs4 import BeautifulSoup

import requests
import webbrowser

# For scraping article and getting its title and body(p tags content)

google = "https://www.google.com/search?q="
url = input("please enter what you want to scrap: ")
url = google+url.replace(" ","+")
url

res = requests.get(url)

html_cont = res.content

data = BeautifulSoup(html_cont,'html.parser')

for i in data.find_all('h3',{'class':"zBAuLc l97dzf"}):
    print(i.text)
