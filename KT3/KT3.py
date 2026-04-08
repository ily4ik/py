import pandas as pd
def get_books(name):
    df = pd.read_csv(name, sep="|", header=0).values.tolist()
    return df

def filtered_books(books, title):
    df = pd.DataFrame(books, columns=['isbn', 'title', 'author', 'quantity', 'price'])
    df = df[df['title'].str.contains(title, case=False, na=False)]
    return df

def mult(books):
    return list(map(lambda b: (b[0], b[4] * b[5]), books))

books = get_books("books.csv")
print(filtered_books(books,"python"))
print(mult(books))
