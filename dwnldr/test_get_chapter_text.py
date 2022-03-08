import requests
from bs4 import BeautifulSoup
from clear_chapter_tags import clear_chapter_tags
from config_reader import get_config

chapter_url = "https://lightnovelreader.org/martial-god-asura-615125/chapter-5037"
config = get_config("https://lightnovelreader.org/martial-god-asura-615125/")


def get_chapters_text(chapter_url, config) -> str:
    """
    """
    page = requests.get(chapter_url)
    soup = BeautifulSoup(page.content, "html.parser")

    chapter_header = eval(config["chapter_name_evaluation_expression"])
    print("Chap header: ", chapter_header)

    chapter_text = eval(config["chapter_text_evaluation_expression"])

    clear_chapter_tags(chapter_text, config)
    print("Chap text:", chapter_text)

    # return chapter_header + "\n" + chapter_text
    return "END"

get_chapters_text(chapter_url, config)