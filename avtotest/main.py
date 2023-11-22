from register import register
from login import login
from author import add_author
from metabook import add_metabook
from book import add_book
from text import add_text
from download_books import download
from cookie import cookie

if __name__ == "__main__":
    register("12", "12345", "asg@gmail.com")
    login("12", "12345")
    add_author("12", "12345", "Gogol", "Гоголь", "Gogol", "Gogol", "1903", "1920")
    add_metabook("12", "12345", "Вий1", "1", "1913", "Gogol")
    add_book("12", "12345", "Вий", "Гоголь", "1913", "Вий1 (1 chapters)")
    add_text("12", "12345", "Вий")
    download("12", "12345")
    cookie()

