from stats import get_book_text
from stats import word_count
from stats import characters
from stats import sort_on
import sys


def main() :
    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    words = word_count(text)
    list = characters(text)
    list.sort(reverse=True, key=sort_on)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for dic in list :
        if dic["name"].isalpha() :
            print(f"{dic["name"]}: {dic["num"]}")
    print("============= END ===============")




main()