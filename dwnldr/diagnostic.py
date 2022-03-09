from .get_authors import get_authors
from .get_novel_name import get_novel_name
from .get_chapters_list import get_chapters_list
from .get_chapters_text import get_chapters_text



def diagnostic(main_url, config, links_url):
    authors = get_authors(main_url, config)
    novel_name = get_novel_name(main_url, config)
    links = get_chapters_list(links_url, config)
    print("Authors: ", authors)
    print("Novel name: ", novel_name)
    print("Links: ", links)
    if len(links) > 0:
        text = get_chapters_text(links[1], config)
        print("Text: ", text)

