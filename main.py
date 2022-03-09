import argparse
from distutils.log import debug  # pragma: no cover
from dwnldr import get_config, \
    get_authors, \
    get_novel_name, \
    get_chapters_list, \
    get_chapters_text, \
    create_html_book, \
    diagnostic
import json
# import logging
# logging.basicConfig(level=logging.INFO, file='downloader.log', format='%(asctime)s :: %(levelname)s :: %(message)s')


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
        "-d",
        "--diagnostic",
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
    config = get_config(main_url)

    if not args.links_source:
        links_url = main_url

    if args.diagnostic:
        diagnostic(main_url=main_url, config=config, links_url=links_url)

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
