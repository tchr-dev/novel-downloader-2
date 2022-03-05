import requests
from bs4 import BeautifulSoup


def get_authors(url, config) -> []:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")

    expr = config["authors_evaluation_expression"]
    author = eval(expr)

    return [author]
