book_path = 'books/frankenstein.txt'
book_open = open(book_path, "r")
book_content = book_open.read()
split_book_content = book_content.split()
word_count = len(split_book_content)
print(word_count)