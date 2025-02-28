from bs4 import BeautifulSoup
import requests

url = 'https://www.pracuj.pl/praca/senior-data-engineer-katowice-wroclawska-54,oferta,1003904240'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')
#print(soup)

tech_list = soup.find_all('span', {'data-test': 'item-technologies-expected'})
#print(tech_list)
for i in tech_list:
    print(i.get_text())