from bs4 import BeautifulSoup
import requests


def scan(offer_list):
    job_dict_list = []
    for offer in offer_list:
        html_text = requests.get(offer).text
        offer_soup = BeautifulSoup(html_text, 'html.parser')
        
        #to find job_title
        h1_tag = offer_soup.find('h1', {'data-test' : 'text-positionName'})
        job_title = h1_tag.getText()

        #to find level
        div = offer_soup.find('div', {'data-test' : 'sections-benefit-employment-type-name-text'})
        level = div.getText()

        #to find technologies
        p_tags = offer_soup.find_all('p', {'data-test': 'text-technology-name'})
        technologies = [i.getText() for i in p_tags]

        #make a dictionary for the offer
        job_dict = {
        'job_title': job_title,
        'level': level,
        'technologies' : technologies
        }
        job_dict_list.append(job_dict)
        

    return job_dict_list
