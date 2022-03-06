import requests
from bs4 import BeautifulSoup
import re


def get_chapters_list(url, config) -> []:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    site_url = config["site_name_regex"]

    data = soup.find_all("a", {"href": re.compile(config[r"chapter_link_regex"])})
    links = list(dict.fromkeys([site_url+item["href"] for item in data]))

    return links
