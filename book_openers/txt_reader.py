"""
Deprecation Warning

use gutenberg.py instead
"""


import re
import os
from pprint import pprint
import pandas as pd
import requests


def main():
    books = os.listdir("books/txt_files")
    test_on_books(books)


samples = [
    43,
    25525,
    98,
    1184,
    215,
    2542,
    1952,
]

generate_aleph_url(samples[3])

r = requests.get("http://aleph.gutenberg.org/1/1/8/1184/1184-0.txt")

text = r.text
text = text.replace("\r", "")
text = text.split("\n")

extract_first_lines_from_file(text)


def test_on_books(books):

    books_info = []

    for book in books:
        with open("books/txt_files/" + book) as f:
            data = f.readlines()
        book_info = extract_first_lines_from_file(data)
        books_info.append(
            {
                "author": book_info["author"],
                "title": book_info["title"],
                "first line": book_info["first_line"],
            }
        )

    df = pd.DataFrame(books_info)

    print(df)


def extract_first_lines_from_file(textfile):

    text_metadata = iterate_through_text(textfile)
    possible_chapters = text_metadata["chapter_ones"]

    possible_lines = []
    chapter_titles = []
    for poss in possible_chapters:
        fs = find_first_sentence(textfile, poss)
        if clean_sentence(fs):
            possible_lines.append(clean_sentence(fs))

        if check_for_chapter_title(textfile, poss):
            chapter_titles.append(check_for_chapter_title(textfile, poss))

    if chapter_titles:
        text_metadata["first_line"] = remove_title_from_first_line(
            possible_lines[0], chapter_titles[0]
        )
    else:
        text_metadata["first_line"] = possible_lines[0]
    text_metadata["chapter_title"] = chapter_titles

    return text_metadata


def iterate_through_text(text_lines):
    """ 
    Multiple things in one method so we only need to iterate through once

    Returns dict:
        chapter_ones [list(int)]: indices of lines starting with "Chapter 1"
        title [str]: title of the book
        author [str]: author of the book

    """
    chapter_one_lines = []
    title = None
    author = None
    for number, line in enumerate(text_lines):
        if re.match("\s*(chapter [I1](?![IVX\d]))", line, flags=re.I):
            chapter_one_lines.append(number)
        elif re.match("title: (.*)", line, re.I):
            title = re.match("title: (.*)", line, re.I)[1]
        elif re.match("author: (.*)", line, re.I):
            author = re.match("author: (.*)", line, re.I)[1]

    return {"chapter_ones": chapter_one_lines, "title": title, "author": author}


def check_for_chapter_title(text_lines, line_number):
    m = re.search("(?<=chapter [1I])(.+)", text_lines[line_number], re.I)

    try:
        output = " ".join([i for i in m[0].split() if i is not "."])
    except:
        pass
    else:
        return output


def find_first_sentence(text_lines, start_line):
    first_lines = []
    for line in text_lines[start_line + 1 :]:
        if re.search("chapter", line, flags=re.I):
            break
        else:
            first_lines.append(line)
            if re.search("[\.\?!]", line):
                break

    return " ".join(first_lines)


def clean_sentence(s):
    clean = s.replace("\n", "")

    try:
        clean = re.search(" ?(.*)[\.\?!]", clean)[0]
    except:
        pass
    else:
        clean = " ".join(clean.split())

    return clean


def remove_title_from_first_line(line, title):
    if re.match(title, line, re.I):
        r = re.compile(title + " (.*)")
        m = re.match(r, line)
        return m[1]

    else:
        return line


def generate_aleph_url(num):

    num = str(num)
    url = "http://aleph.gutenberg.org/"

    for i in num[:-1]:
        url = url + f"{i}/"

    url = url + f"{num}/{num}.txt"

    return url


if __name__ == "__main__":
    main()
