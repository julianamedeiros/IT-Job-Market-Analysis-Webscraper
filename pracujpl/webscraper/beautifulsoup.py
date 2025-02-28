from bs4 import BeautifulSoup
import requests


def scan(offer_list):
    job_dict_list = []

    for offer in offer_list:
        html_text = requests.get(offer).text
        offer_soup = BeautifulSoup(html_text, 'html.parser')

        # To extract job title
        h1_tag = offer_soup.find('h1', {'data-test' : 'text-positionName'})
        job_title = h1_tag.getText()

        # To extract job level
        div = offer_soup.find('li', {'data-test' : 'sections-benefit-employment-type-name'})
        level = div.getText()

        # To extract demanded technologies
        technologies = []
        tech_list = offer_soup.find_all('span', {'data-test': 'item-technologies-expected'})
        #print(tech_list)
        for i in tech_list:
            tech = i.get_text()
            technologies.append(tech)


        # Store offer details in a dictionary
        job_dict = {
        'job_title': job_title,
        'level': level,
        'technologies' : technologies
        }
        job_dict_list.append(job_dict)
        

    return job_dict_list
