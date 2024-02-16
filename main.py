from package import primary
from package import secondary
from package import tertiary
from package import datavisualization

def main():
    url = primary.search_job('data engineer')
    offer_list = secondary.list_offer(url)
    job_dict_list = tertiary.scan(offer_list)
    datavisualization.table(job_dict_list)


if __name__ == "__main__":
    main()