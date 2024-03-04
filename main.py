from package import webcrawler
from package import urlparsing
from package import webscrapper
from package import dataprocessing

def main():
    url = webcrawler.search_job('data analyst')
    offer_list = urlparsing.list_offer(url)
    job_dict_list = webscrapper.scan(offer_list)
    dataprocessing.star_scheme(job_dict_list)


if __name__ == "__main__":
    main()