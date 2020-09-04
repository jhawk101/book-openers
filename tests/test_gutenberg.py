from book_openers.gutenberg import Book
import pytest


def test_alice():
    alice = Book("book_openers/txt_files/alice.txt")
    assert alice.title == "Alice’s Adventures in Wonderland"
    assert alice.author == "Lewis Carroll"
    assert alice._chapter_ones == [38, 54]
    assert alice._chapter_one_title == "Down the Rabbit-Hole"
    assert alice.first_line == (
        "Alice was beginning to get very tired of sitting by her sister on the "
        "bank, and of having nothing to do: once or twice she had peeped into "
        "the book her sister was reading, but it had no pictures or "
        "conversations in it, “and what is the use of a book,” thought Alice "
        "“without pictures or conversations?"
    )


@pytest.mark.skip(reason="slow to call url every time")
def test_count():
    count = Book(
        "http://aleph.gutenberg.org/1/1/8/1184/1184-0.txt", init_from="url"
    )
    assert count.title == "The Count of Monte Cristo"
    assert count.author == "Alexandre Dumas, pÃ¨re"
    assert count._chapter_ones == [55, 187]
    assert count._chapter_one_title == "Marseillesâ\x80\x94The Arrival"
    assert count.first_line == (
        "On the 24th of February, 1815, the look-out at Notre-Dame de la Garde "
        "signalled the three-master, the _Pharaon_ from Smyrna, Trieste, and "
        "Naples."
    )
