def get_books(name):
    with open(name, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return list(map(lambda line: line.split('|'), lines[1:]))

def filtered_books(books, title_substring):
    return list(filter(lambda book: title_substring.lower() in book[1].lower(),books))

def mult(books):
    return list(map(lambda book: (book[0], int(book[3]) * float(book[4])),books))

books = get_books("books.csv")
print(filtered_books(books, "python"))
print(mult(books))
