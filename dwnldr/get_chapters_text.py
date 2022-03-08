import requests
import re
from bs4 import BeautifulSoup
from .clear_chapter_tags import clear_chapter_tags


def get_chapters_text(chapter_url, config) -> str:
    """
    """
    page = requests.get(chapter_url)
    soup = BeautifulSoup(page.content, "html.parser")

    chapter_header = eval(config["chapter_name_evaluation_expression"])
    chapter_text = eval(config["chapter_text_evaluation_expression"])
    clear_chapter_tags(chapter_text, config)

    return chapter_header + "\n" + str(chapter_text)
