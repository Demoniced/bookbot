def main():
    book_path = "books/frankenstein.txt"
    book = book_text(book_path)
    num_words = count_words(book)
    # print(f"{num_words} words found in the book")
    char_count = char_counter(book)
    list_dict = creat_list_dict(char_count)
    list_dict.sort(key=sort_on,reverse=True)
    # print(list_dict)
    report = book_report(book_path,num_words,list_dict) 
    
name = []
#Returns the number of words in the book
def count_words(text):
    words = text.split()
    return len(words)
#creates a dictionary of characters and increments the times they are used.
def char_counter(char):
    words = list(char.lower())
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = {}
    for letter in words:
        if letter in alphabet:
            if letter not in count:
                count[letter] = 1
            else:
                count[letter] += 1
    return count

             
#opens the file and returns the text
def book_text(path): 
    with open(path) as f:
        return f.read()

def creat_list_dict(dict):
    for key in dict:
        name.append({"letter":key,"num":dict[key]})
    return name

def sort_on(dict):
    return dict["num"]
    
def book_report(book_path,num_words,list_dict):
    print(f"--- Begin report of {book_path}---")
    print(f"{num_words} words found in the document")
    for item in list_dict:
        print(f"The {item['letter']} character was found {item['num']} times")
    print("--- End report ---")    

      
main()
