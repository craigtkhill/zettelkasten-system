from sys import argv
from datetime import datetime

quotes = {}
book_quotes = []

# get the current date as a string
def get_date():
    return datetime.now().strftime("%Y-%m-%d")

date = get_date()

with open(f"kindle-notes/{date}.txt", "r", encoding="utf-8") as f:
    book_quotes.extend(line for line in f if not line.startswith(("-", "\n", "=")))
for i in range(len(book_quotes)):
    if i % 2 == 0:
        if book_quotes[i] not in quotes:
            quotes[book_quotes[i]] = []
    else:
        quotes[book_quotes[i - 1]].append(book_quotes[i])

with open(f"zettel-notes/{date}.md", "w+", encoding="utf-8") as f:
    for book, quote in quotes.items():
        f.write(f"## {book.upper()}\n")
        for line in quote:
            f.write(f"{line}\n")




