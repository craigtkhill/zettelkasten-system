from sys import argv

quotes = {}
book_quotes = []

with open(f"kindle-notes/{argv[0]}.txt", "r", encoding="utf-8") as f:
    book_quotes.extend(line for line in f if not line.startswith(("-", "\n", "=")))
for i in range(len(book_quotes)):
    if i % 2 == 0:
        if book_quotes[i] not in quotes:
            quotes[book_quotes[i]] = []
    else:
        quotes[book_quotes[i - 1]].append(book_quotes[i])

with open(f"../zettelkasten-notes/{argv[1]}.md", "w+", encoding="utf-8") as f:
    for book, quote in quotes.items():
        f.write(f"## {book.upper()}\n")
        for line in quote:
            f.write(f"{line}\n")




