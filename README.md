# Book openers

Making a dataset of opening lines to texts using the open data from the guttenberg project.

## Motivation

I wanted to make an online version of the game [ex libris](https://en.wikipedia.org/wiki/Ex_Libris_%28game%29), which requires players to write fake first lines of books. I couldn't find a dataset of first lines online, so had a look at [Project Gutenberg](http://www.gutenberg.org/) to see if I could make a dataset.

## Approach

There are multiple file types available on Gutenberg (html, epub, kindle, plain txt, pdf). There didn't seem to be an advantage in using one of the more complex file types, so I focussed on the plain text.

The texts are prepended with a lot of irrelevant detail such as licencing before getting into the main body. My approach for collecting first lines was to:

* Use regex to find lines in the text containing "Chapter One/1/I"
* Identify the title for Chapter One, if it appears on the same row as the regex
* Scan from "Chapter One" until the next full stop, saving the text
* Remove the title of the chapter from this text, if necessary
* Clean the text of carriage returns etc. if necessary

## Packages

Used [gutenbergpy](https://github.com/raduangelescu/gutenbergpy) as a wrapper to query the database. It hasn't been updated for python 3 so had to edit `textget.py` imports in my virtualenv:

``` python
import http.client as httplib
..
from urllib.request import urlopen
from urllib.parse import urlparse
```
