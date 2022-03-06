import argparse
from distutils.log import debug  # pragma: no cover
from dwnldr import get_config, get_authors, get_novel_name, get_chapters_list, get_chapters_text
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

    args = parser.parse_args()
    url = args.url

    if args.config:
        config = get_config(url)
        authors = get_authors(url, config)
        novel_name = get_novel_name(url, config)
        links = get_chapters_list(url, config)
        text = get_chapters_text(links[1], config)
        print(authors)
        print(novel_name)
        # print(links)
        print(text)

    print(f"-" * 10 + "END" + f"-" * 10)


if __name__ == "__main__":  # pragma: no cover
    main()
