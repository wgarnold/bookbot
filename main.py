def main(): # passes the path to get_book_text function and prints returned text.
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f"{num_words} words found in the document")


def get_book_text(path): # takes the book path, opens and then reads to a string
    with open(path) as f:
        return f.read()

def word_count(book_text):
    words = book_text.split()
    return len(words)

main()
