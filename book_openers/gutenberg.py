import gutenbergpy.textget as tget
from book_openers.book import Book

"""
NOTES

43 - Jekyll & Hyde, could just take the first sentence (exclude title, author, chapter name) 
    if no chapter 1s are found
2417 - Complete Poe, not doable 
'http://aleph.gutenberg.org/2/1/4/2147/2147-0.txt'

98 - tale of two cities, done
'http://aleph.gutenberg.org/9/98/98.txt',

1184 - count of monte cristo. done, v slow.
'http://aleph.gutenberg.org/1/1/8/1184/1184-0.txt',

215 - The call of the wild, done, slow.
'http://aleph.gutenberg.org/2/1/215/215.txt',

2542 - A Doll's House - a play, would need to be from 'ACT I'
'http://aleph.gutenberg.org/2/5/4/2542/2542.txt',

1952 - The Yellow Wallpaper - similar to J&H, first complete para would do it
'http://aleph.gutenberg.org/1/9/5/1952/1952.txt'
"""

EXAMPLE_IDS = [
    # 43,
    # 2147,
    98,
    # 1184,
    # 215,
    # 2542,
    # 1952,
]


def main():
    for book_id in EXAMPLE_IDS:
        url = tget._format_download_uri(book_id)
        book = Book(url, source_type="url")
        print(book.title)
        print(book.author)
        print(book.first_line)
        print("\n")
