from pracujpl import webcrawler
from pracujpl import urlparsing
from pracujpl import webscrapper
from pracujpl import dataprocessing

def main():
    url = webcrawler.search_job('data analyst')
    offer_list = urlparsing.list_offer(url)
    job_dict_list = webscrapper.scan(offer_list)
    dataprocessing.star_scheme(job_dict_list)


if __name__ == "__main__":
    main()