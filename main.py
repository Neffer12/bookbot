from stats import word_count
from stats import character_count
from stats import sorted_list
import sys

if len(sys.argv)!=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text(sys.argv[1])
    count = word_count(book_text)
    character = character_count(book_text)
    sorted_chars = sorted_list(character)
    #print(f"{count} words found in the document")
    #print(f"{character}")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ------------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        #Only print if an alphabetical character
        if char.isalpha():
            print(f"{char}: {count}:")
    
    print("============= END ===============")


main()