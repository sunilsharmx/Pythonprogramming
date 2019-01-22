#!/usr/bin/env python

"""Retreive and print words from a URL
Usage:
    python urllibeg.py <URL>
"""
import sys
from urllib.request import urlopen
#http://sixty-north.com/c/t.txt
def fetch_words(url):
    """Fetch a list of words from URL
    Args:
        url: The URL of UTF-8 text document
    Returns:
        A List of strings containing the words
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return(story_words)


def print_items(items):
    for item in items:
        print(item)

def main(url):
    words=fetch_words(url)
    print_items(words)
if __name__ == "__main__":
   main(sys.argv[1])