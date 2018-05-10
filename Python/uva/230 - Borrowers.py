books = []
while True:
    try:
        title, author = map(str, input().split("by"))
        books.append((title.strip(), author.strip()))
    except ValueError:
        break