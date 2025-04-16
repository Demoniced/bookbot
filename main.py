from stats import word_count
from stats import character_counter
from stats import report
import sys
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
def report_printer(report,words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char in report:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["count"]}")
    print("============= END ===============")       

def main():
    #print(get_book_text("books/frankenstein.txt"))
        try:
            if sys.argv[0] and [1]:
                report_printer(report(character_counter(get_book_text(sys.argv[1]))),word_count(get_book_text(sys.argv[1])))

        except Exception:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
            
        
    #print(report(character_counter(get_book_text("books/frankenstein.txt"))))
    #print(word_count(get_book_text("books/frankenstein.txt")))
    #print(character_counter(get_book_text("books/frankenstein.txt")))
main()