from scrape_jobs import *
from json import dumps


def dict_list_to_json(dict_list, filename):
    """
    Writes a list of dictionaries to a json file
    - dict_list: list of dictionaries
    - filename: name of the file to write to
    """
    with open(filename, "w") as file:
        file.write(dumps(dict_list, indent=4))


def test_json_writer():
    """
    Tests the json writer
    - creates a chromedriver path
    - creates a url
    - scrapes the jobs
    - writes the jobs to a file named jobs.json
    """
    # create the chromedriver path
    chromedriver_path = create_chromedriver_path()

    # create the url
    url = create_scraping_url("Software", "Charlotte")

    # scrape the jobs
    jobs = scrape_jobs(chromedriver_path, url)

    # write the jobs to a file
    dict_list_to_json(jobs, "jobs.json")


if __name__ == "__main__":
    test_json_writer()
