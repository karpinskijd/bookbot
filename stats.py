def sort_on(items):
    return items["num"]

def count_words(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter

def count_chars(text):
    chars = text.lower()
    char_count = {}
    for char in chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

