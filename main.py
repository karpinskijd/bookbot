def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters_count = count_characters(text)
    num_characters = filter_and_sort_characters(characters_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for character, count in num_characters:
        print(f"The '{character}' character was found {count} times")
        
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = {}
    for character in text:
        #convert to lowercase for case-insensitive counting
        lc = character.lower()
        if lc in chars:
            chars[lc] += 1
        else:
            chars[lc] = 1
    return chars

def filter_and_sort_characters(chars):
    #filter out non-letters and sort by character count
    result_list = [(letter, count) for letter, count in chars.items() if letter.isalpha()]
    result_list.sort(key=lambda x: x[1], reverse=True)
    return result_list


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()