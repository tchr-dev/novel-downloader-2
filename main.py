import argparse
from distutils.log import debug  # pragma: no cover
from dwnldr import get_config, \
    get_authors, \
    get_novel_name, \
    get_chapters_list, \
    get_chapters_text, \
    create_html_book
import json


def main() -> None:  # pragma: no cover
    """
    The main function executes on commands:
    `python -m project_name` and `$ project_name `.

    """
    print(f"-"*10+"Start"+f"-"*10)
    parser = argparse.ArgumentParser(
        description="web-novel downloader.",
        epilog="Enjoy the web-novel downloader functionality!",
    )
    # This is required positional argument
    parser.add_argument(
        "url",
        type=str,
        help="Web-novel main url",
        default="url",
    )

    parser.add_argument(
        "-c",
        "--config",
        action="store_true"
    )

    parser.add_argument(
        "-l",
        "--links_source",
        action="store",
        type=str,
        help="source of links list"
    )

    parser.add_argument(
        "-b",
        "--book_html",
        action="store_true"
    )

    args = parser.parse_args()
    main_url = args.url
    links_url = args.links_source

    if not args.links_source:
        links_url = main_url

    if args.config:
        config = get_config(main_url)
        authors = get_authors(main_url, config)
        novel_name = get_novel_name(main_url, config)
        links = get_chapters_list(links_url, config)
        # text = get_chapters_text(links[1], config)
        print(authors)
        print(novel_name)
        # print(links)
        # print("Links: ", links[1])
        # print("Text: ", text)

    if args.book_html:
        print("Creating book")
        config = get_config(main_url)
        authors = get_authors(main_url, config)
        novel_name = get_novel_name(main_url, config)
        links = get_chapters_list(links_url, config)
        create_html_book(authors, novel_name, links, config)

    print(f"-" * 10 + "END" + f"-" * 10)


if __name__ == "__main__":  # pragma: no cover
    main()
