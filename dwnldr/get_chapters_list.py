import requests
from bs4 import BeautifulSoup
import re


def get_chapters_list(url, config) -> []:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    site_url = config["site_name_regex"]

    data = eval(config["chapter_links_evaluation_expression"])
    # links = list(dict.fromkeys([site_url+item["href"] for item in data]))
    links = list(dict.fromkeys(el for el in data))

    return links
