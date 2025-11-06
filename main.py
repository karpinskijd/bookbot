import sys
from stats import count_words, count_chars

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    sorted_chars = count_chars(text)

    print(
        "============ BOOKBOT ============\n" 
        f"Analyzing book found at {sys.argv[1]}...\n"
        "----------- Word Count ----------\n"
        f"Found {num_words} total words\n"
        "--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print(
        "============= END ==============="
    )

main()
