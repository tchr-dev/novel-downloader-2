import requests
from bs4 import BeautifulSoup


def get_novel_name(url, config) -> str:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")

    print(soup.find("h1").contents)

    # expr = config["novel_name_evaluation_expression"]
    # author = eval(expr)

    return ""
