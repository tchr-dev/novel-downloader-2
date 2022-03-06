import requests
from bs4 import BeautifulSoup


def get_novel_name(url, config) -> str:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")

    novel_name = eval(config["novel_name_evaluation_expression"])

    # expr = config["novel_name_evaluation_expression"]
    # author = eval(expr)

    return novel_name
