from bs4 import BeautifulSoup
import requests

def list_offer(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    a_tags = soup.find_all('a', {'data-test': 'link-offer'})  
    offer_list = [a_tag['href'] for a_tag in a_tags]
    return offer_list

