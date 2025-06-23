from stats import word_count # import word count function
from stats import char_count
def main(): # passes the path to get_book_text function and prints returned text.
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    characters = char_count(text)
    print(f"{num_words} words found in the document")
    print(characters)


def get_book_text(path): # takes the book path, opens and then reads to a string
    with open(path) as f:
        return f.read()

main()
