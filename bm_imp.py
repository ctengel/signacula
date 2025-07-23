"""Tools for importing browser bookmark files into signicula"""

import pathlib
import argparse
import bookmarks_converter

API = 'http://127.0.0.1:8000'

def recurse_urls(folder):
    """Recurse and extract URLs from a folder object"""
    # TODO add in titles etc
    url_list = []
    if hasattr(folder, "url"):
        url_list.append(folder.url)
    if hasattr(folder, "children"):
        url_list = []
        for child in folder.children:
            url_list = url_list + recurse_urls(child)
    return url_list

def read_bookmarks(filename):
    """Read bookmarks from file and return URLs"""
    bookmarks = bookmarks_converter.Firefox().from_json(pathlib.Path(filename))
    return recurse_urls(bookmarks)

def cli():
    """CLI"""
    # TODO add in an option for other formats
    # TODO actually convert to API
    parser = argparse.ArgumentParser()
    parser.add_argument("jsonfile")
    args = parser.parse_args()
    print(read_bookmarks(args.jsonfile))

if __name__ == '__main__':
    cli()
