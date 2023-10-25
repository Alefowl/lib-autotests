from register import register
from login import *
from author import add_author
from metabook import add_metabook
from book import add_book
from text import add_text
from download_books import download

if __name__ == "__main__":
    register()
    login()
    add_author()
    add_metabook()
    add_book()
    add_text()
    download()
