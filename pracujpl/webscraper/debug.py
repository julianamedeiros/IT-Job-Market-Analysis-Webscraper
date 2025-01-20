from bs4 import BeautifulSoup
import requests

url = 'https://www.pracuj.pl/praca/data-scientist-warszawa-opatowska-2,oferta,1003801175?s=fd093a39&searchId=MTczNzM5NTcyNjU4NC4yOTE3&ref=top_boosterAI_L2_5_1_1'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')
#print(soup)

tech_list = soup.find_all('span', {'class' : '_chip_ga1vw_1 _chip--light_ga1vw_1 _chip--large_ga1vw_1 _chip--full-corner_ga1vw_1 ez2hkn'})
#print(tech_list)
for i in tech_list:
    print(i.get_text())