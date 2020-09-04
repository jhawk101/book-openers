import re
import requests


class Gutenberg:
    def __init__(self, init_arg, init_from="txt"):
        self.init_arg = init_arg
        if init_from == "txt":
            self.init_from_text_file(self.init_arg)
        else:
            self.init_from_url(self.init_arg)

    def init_from_text_file(self, filepath):
        with open(filepath) as f:
            self.lines_of_text = f.readlines()

    def init_from_url(self, url):
        r = requests.get(url)
        text = r.text
        text = text.replace("\r", "")
        self.lines_of_text = text.split("\n")

    @property
    def title(self):
        line = 0
        title = ""
        while not title:
            if re.match("title: (.*)", self.lines_of_text[line], re.I):
                title = re.match("title: (.*)", self.lines_of_text[line], re.I)[
                    1
                ]
            line += 1
        return title

    @property
    def author(self):
        line = 0
        author = ""
        while not author:
            if re.match("author: (.*)", self.lines_of_text[line], re.I):
                author = re.match(
                    "author: (.*)", self.lines_of_text[line], re.I
                )[1]
            line += 1
        return author

    @property
    def _chapter_ones(self):
        rows = []
        for number, line in enumerate(self.lines_of_text):
            if re.match(r"\s*(chapter [I1](?![IVX\d]))", line, flags=re.I):
                rows.append(number)
        return rows

    @property
    def _chapter_one_title(self):
        if not self._chapter_ones:
            return ""

        for row in self._chapter_ones:
            m = re.search(
                r"(?<=chapter [1I])(.+)", self.lines_of_text[row], re.I
            )

            try:
                output = " ".join([i for i in m[0].split() if i is not "."])
            except:
                return ""
            else:
                return output

    def _sentence_after_chapter(self, row):
        sentence = []
        for line in self.lines_of_text[row + 1 :]:
            if re.search("chapter", line, flags=re.I):
                break
            else:
                sentence.append(line)
                if re.search(r"[\.\?!]", line):
                    break

        return " ".join(sentence)

    def _remove_title_from_first_line(self, sentence):
        if re.match(self._chapter_one_title, sentence, re.I):
            r = re.compile(self._chapter_one_title + " (.*)")
            m = re.match(r, sentence)
            return m[1]

        else:
            return sentence

    @property
    def first_line(self):
        options = []
        for row in self._chapter_ones:
            sentence = self._sentence_after_chapter(row)
            if sentence:
                clean = sentence.replace("\n", " ")
                cleaner = re.search(r" ?(.*)[\.\?!]", clean)[0]
                cleanest = " ".join(cleaner.split())
                final = self._remove_title_from_first_line(cleanest)
                options.append(final)

        return options[0]
