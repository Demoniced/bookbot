from stats import word_count
from stats import character_counter
from stats import report

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
def report_printer(report):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found 75767 total words")
    print("--------- Character Count -------")
    for char in report:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["count"]}")
    print("============= END ===============")       

def main():
    #print(get_book_text("books/frankenstein.txt"))
    report_printer(report(character_counter(get_book_text("books/frankenstein.txt"))))
    #print(report(character_counter(get_book_text("books/frankenstein.txt"))))
    #print(word_count(get_book_text("books/frankenstein.txt")))
    #print(character_counter(get_book_text("books/frankenstein.txt")))
main()