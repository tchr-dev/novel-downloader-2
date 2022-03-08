import re

chapter_url=" https://lightnovelreader.org/the-protagonists-are-murdered-by-me/chapter-245"

chapter_header = re.search(r"[Cc].apter\s*-[\d*-.\d*]", chapter_url).group(0)

print(chapter_header)