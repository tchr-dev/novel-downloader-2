from tqdm import tqdm
import re
from dwnldr import get_chapters_text


def create_html_book(authors, novel_name, links, config):
    """

    """

    # HTML Structure
    html_boilerplate_start = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <meta name="author" content="{", ".join(authors)}">
            <title>{novel_name}</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
        """

    html_boilerplate_end = """
        </body>
        </html>
        """

    novel_name = re.sub(r'[^a-zA-Zа-яА-Я0-9 \n\.]', '', novel_name)
    book_name = novel_name + '.html'

    with open(book_name, "w") as output_html:
        output_html.writelines(html_boilerplate_start)

        if len(links) > 0:
            pbar = tqdm(total=len(links) + 1)
            for chapter_link in links:
                # chapter_number = re.search(r"\d+-?\d$", chapter_link).group(0)
                # print("Chapter num: ", chapter_number)
                output_html.write(get_chapters_text(
                    chapter_url=chapter_link, config=config))
                pbar.update(1)
            pbar.close()

        output_html.writelines(html_boilerplate_end)

        output_html.close()
