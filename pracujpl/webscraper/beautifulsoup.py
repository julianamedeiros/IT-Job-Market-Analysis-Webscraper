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
        div = offer_soup.find('li', {'data-test' : 'sections-benefit-employment-type-name'})
        level = div.getText()

        #to find technologies
        technologies = []
        tech_list = offer_soup.find_all('span', {'class' : '_chip_ga1vw_1 _chip--light_ga1vw_1 _chip--large_ga1vw_1 _chip--full-corner_ga1vw_1 ez2hkn'})
        #print(tech_list)
        for i in tech_list:
            tech = i.get_text()
            technologies.append(tech)



        #make a dictionary for the offer
        job_dict = {
        'job_title': job_title,
        'level': level,
        'technologies' : technologies
        }
        job_dict_list.append(job_dict)
        

    return job_dict_list
