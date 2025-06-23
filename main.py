from curses.ascii import isalpha
from stats import (
    word_count,
    char_count,
    chars_dict_to_sorted_list,
)
def main(): # passes the path to get_book_text function and prints returned text.
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    characters = char_count(text)
    char_sorted_list = chars_dict_to_sorted_list(characters)
    # print(f"{num_words} words found in the document")
    print_report(book_path, num_words, char_sorted_list)


def get_book_text(path): # takes the book path, opens and then reads to a string
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, char_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_sorted_list:
        if not item["char"].isalpha():
           continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")



main()
