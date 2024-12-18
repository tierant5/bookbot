
def report(num_words, num_chars):
    print("--- Begin report of books/frankenstein.txt --- ")
    print(f"{num_words} words found in the document")
    print("\n")
    for char, count in num_chars.items():
        print(f"The '{char}' character was found {count} times")

def num_chars(text):
    chars = {}
    for char in text:
        char = char.lower()
        if char not in chars.keys():
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def num_words(text):
    text_list = text.split()
    return len(text_list)

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

    report(num_words(file_contents), num_chars(file_contents))

main()
