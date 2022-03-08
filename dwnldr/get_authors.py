import requests
from bs4 import BeautifulSoup


def get_authors(url, config) -> []:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    authors=[]

    # authors = [eval(expr) for expr in config["authors_evaluation_expression"]]
    for expr in config["authors_evaluation_expression"]:
        authors.extend([eval(expr)])

    return authors
