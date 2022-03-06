import requests
from bs4 import BeautifulSoup


def get_chapters_text(config, chapter_list) -> str:
    """
    """
    url = chapter_list[1]
    # print(chapter_list[1])
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")

    chapter_header = str(soup.find("h1"))
    chapter_text = str(soup.find("div", class_="content-text"))

    return chapter_header + "\n" + chapter_text
