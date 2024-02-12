from package import primary
from package import secondary


def main():
    url = primary.search_job('data analyst')
    secondary.list_jobs(url)


if __name__ == "__main__":
    main()