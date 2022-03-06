import requests
from bs4 import BeautifulSoup
from .clear_chapter_tags import clear_chapter_tags


def get_chapters_text(chapter_url, config) -> str:
    """
    """
    page = requests.get(chapter_url)
    soup = BeautifulSoup(page.content, "lxml")

    clear_chapter_tags(soup, config)

    chapter_header = eval(config["chapter_name_evaluation_expression"])
    chapter_text = eval(config["chapter_text_evaluation_expression"])

    return chapter_header + "\n" + chapter_text
