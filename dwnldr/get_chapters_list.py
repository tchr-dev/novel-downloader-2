import requests
from bs4 import BeautifulSoup
import re
import logging


def get_chapters_list(url, config) -> []:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    site_url = config["site_name_regex"]
    data = eval(config["chapter_links_evaluation_expression"])
    links = list(dict.fromkeys(el for el in data))

    if len(links[0]) > 0 and re.search(site_url, links[0]) is None:
        links = [site_url + link for link in links]

    # print(links)

    return links
