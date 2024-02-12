from bs4 import BeautifulSoup
import requests


def list_jobs(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    a_tags = soup.find_all('a', {'data-test': 'link-offer'})  
    for i in range(len(a_tags)):
        href = a_tags[i]['href']
        print(href)

