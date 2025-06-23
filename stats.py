def word_count(book_text):
    words = book_text.split()
    return len(words)

def char_count(book_text):
    # converts text to lower case
    lower_case_text = book_text.lower()
   # empty dictionary
    char_dict = {}
    for char in lower_case_text:
        # if character is already in the dict, adds one to its value
        if char in char_dict:
            char_dict[char] += 1
        # else adds to character to the dict with a value of 1
        else:
            char_dict[char] = 1
    return char_dict
