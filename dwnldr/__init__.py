# from .base import BaseClass, base_function
from .config_reader import get_config
from .get_authors import get_authors
from .get_novel_name import get_novel_name
from .get_chapters_list import get_chapters_list
from .get_chapters_text import get_chapters_text
from .clear_chapter_tags import clear_chapter_tags

__all__ = [
    "get_config",
    "get_authors",
    "get_novel_name",
    "get_chapters_list",
    "get_chapters_text",
    "clear_chapter_tags"
]
