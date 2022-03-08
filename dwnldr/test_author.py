import requests
from bs4 import BeautifulSoup

my_url = "https://lightnovelreader.org/the-protagonists-are-murdered-by-me"
my_config = {"authors_evaluation_expression": "soup.find('dt', text='Author(s):').next_sibling.text"}


def get_authors(url, config) -> []:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    author = str.strip(soup.find("dt", text="Author(s):").find_next_sibling().text)
    print(author)

    # expr = config["authors_evaluation_expression"]
    # author = eval(expr)

    return ["author"]


print(get_authors(my_url, my_config))

