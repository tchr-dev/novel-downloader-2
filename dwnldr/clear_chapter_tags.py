import re
from bs4 import BeautifulSoup


def clear_chapter_tags(soup, config) -> BeautifulSoup:
    """

    """
    if type(soup) == str:
        soup = BeautifulSoup(soup, "html.parser")

    tag_list = config["remove_tag_list"]
    class_list = config["remove_class_list"]
    regex_list_with_tag = config["remove_regex_with_tag_list"]

    if len(tag_list) > 0:
        for tag in tag_list:
            found_tags = soup.find_all(tag)
            for el in found_tags:
                el.decompose()

    if len(class_list) > 0:
        for single_class in class_list:
            found_tags = soup.find_all(class_=single_class)
            for el in found_tags:
                el.decompose()

    if len(regex_list_with_tag) > 0:
        for regex_with_tag in regex_list_with_tag:
            found_tags = soup.find_all(regex_with_tag["tag"], string=re.compile(regex_with_tag["regex"]))
            for el in found_tags:
                el.decompose()

    return soup