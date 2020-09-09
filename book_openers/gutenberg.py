import gutenbergpy.textget as tget
from book_openers.book import Book

EXAMPLE_IDS = [
    43,
    25525,
    98,
    1184,
    215,
    2542,
    1952,
]


def main():
    for book_id in EXAMPLE_IDS:
        raw_book = tget.get_text_by_id(book_id)
        book = Book(raw_book)
        print(book.title)
        print(book.author)
        print(book.first_line)
        print("\n")
