import re
from bs4 import BeautifulSoup

txt = "<p>What is the definition of ‘protagonist?’</p> <p>It varies from person to person, but I’m referring to the " \
       "selfish people who" \
       "grew up eating the blessings of the whole world by themselves.</p> <p>Furthermore, as the 21st century has " \
       "changed," \
       " there hasn’t been any ‘crisis’ for the protagonists to deal with.</p> <p>They’re outdated characters.</p> " \
       "<p>In the past they’d die, their girlfriends would die, their families would die, their friends would die, " \
       "or their colleagues would die.</p> <p>What about these days?</p> <p>There’s absolutely no such thing.</p> " \
       "<p>Nowadays the protagonists just know everything, never put their acquaintances in danger, and overwhelm " \
       "everything " \
       "with more power than a villain has.</p> <p>However, the two protagonists I’ve hunted so far were very weak " \
       "for a protagonist.</p>" \
       "<p>One was the ‘tutorial’ and the other was because I was lucky enough to hunt it when it was " \
       "sealed.</p><p>The most " \
       "up-to-date novels are published on lightnovelpub[.]com</p><br/><br/> <br/><br/> <p>Then.</p> <p>What about a " \
       "protagonist " \
       "who just started their prologue?</p> <p>[2…1…0]</p> <p>[Travel Completed.]</p> <p>[You are a hunter who came " \
       "to attack " \
       "Snow Peak of Paulownia.]</p> <p>[The protagonist, Lee Yeonjun, is Level 63.]</p> <p>‘Crazy…’</p> <p>Shortly " \
       "after entering " \
       "the dungeon I had a sour expression, and Celeste who noticed it tilted her head.</p> <p>“Let’s listen to the " \
       "briefing first.”</p>" \
       "<p>The source of this content is lightnovelpub[.]com</p> <p>Let’s think about it.</p> <p>The level of the " \
       "first protagonist " \
       "I hunted was 33.</p> <p>Not to mention his strength, his movements and controls were enough to impress me " \
       "when I first saw it. "

soup = BeautifulSoup(txt, "html.parser")

config = {

    "remove_tag_list": ["div", "center"],
    "remove_class_list": "display-hide",
    "remove_regex_with_tag_list": [{"tag": "p", "regex": "http://tl.rulate.ru"}]
}


def clear_chapter_tags(soup, config):
    """

    """
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

    print(soup.prettify())


clear_chapter_tags(soup, config)
