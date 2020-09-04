"""
How to use this to scrape lines

- wget to pull epubs from project gutenberg - https://www.gutenberg.org/wiki/Gutenberg:Information_About_Robot_Access_to_our_Pages
    commands:
        -w 2
        wait for 2 seconds between retrieval
        -m
        turns mirroring on
        -H
        Enable spanning across hosts when doing recursive retrieving
- see top_100_290520.txt for wget script to pull 100 txt files, have downloaded 5
- ebooklib reads epubs, although might be more sensible to download .txt files and read those
- eg. find "chapter 1|chapter I|I" and then take the next line up

"""


import ebooklib
from ebooklib import epub
from pprint import pprint

book = epub.read_epub("books/moby.epub")

with open("books/end.html", "wb") as f:
    f.write(book.items[27].content)

[
    "id",
    "file_name",
    "media_type",
    "content",
    "is_linear",
    "manifest",
    "book",
    "title",
    "lang",
    "direction",
    "media_overlay",
    "media_duration",
    "links",
    "properties",
    "pages",
]


def print_next_line(book):
    item = next(book.get_items())

    while item.get_type() != ebooklib.ITEM_DOCUMENT:
        item = next(book.get_items())
    print("NAME : ", item.get_name())
    print(item.get_content())
