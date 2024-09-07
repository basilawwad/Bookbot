def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_chars(text)
    print(f"{num_words} words found in the document")
    print(char_count)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_chars(text):
    joined_text = text.replace(' ', '').lower()
    text_map = dict()
    for char in joined_text:
        if char in text_map:
            text_map[char] = text_map[char] + 1
        else:
            text_map[char] = 1
    return text_map

main()
