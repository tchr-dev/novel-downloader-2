import requests
from bs4 import BeautifulSoup
import re

my_url = "https://lightnovelreader.org/martial-god-asura-615125/chapter-5038"
conf= {
    "site_name_regex": "https://lightnovelreader.org",
    "chapter_link_regex": r"https://[-a-zA-Z0-9@:%._\+~#=]{1,256}/[-a-zA-Z0-9@:%._\+~#=]{1,256}/chapter[-0-9.]{1,10}",
}


def get_chapters_list(my_url, config) -> []:
    page = requests.get(my_url)
    soup = BeautifulSoup(page.content, "html.parser")
    site_url = config["site_name_regex"]

    data = [el["value"] for el in soup.find_all("option", {"value": re.compile(config["chapter_link_regex"])})]
    result_list = list(dict.fromkeys(el for el in data))

    return result_list


my_list = get_chapters_list(my_url, conf)
print(my_list)