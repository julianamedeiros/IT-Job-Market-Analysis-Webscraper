
from webscraper import beautifulsoup
from webscraper import webcrawler
from webscraper import urlparsing
from webscraper import processing


def main():
    url = webcrawler.search_job('data analyst')
    offer_list = urlparsing.list_offer(url)
    job_dict_list = beautifulsoup.scan(offer_list)
    processing.cleaning(job_dict_list)


if __name__ == "__main__":
    main()