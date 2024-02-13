from package import primary
from package import secondary
from package import tertiary


def main():
    url = primary.search_job('data engineer')
    offer_list = secondary.list_offer(url)
    tertiary.scan(offer_list)


if __name__ == "__main__":
    main()