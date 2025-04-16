def word_count(text):
    text_string = text.split()
    word_counter = 0
    for word in text_string:
        word_counter +=1
    return word_counter
def character_counter(char):
    text_string = char.split()
    joined = ' '.join(text_string)
    tracker = {}
    for word in joined.lower():
        if word not in tracker:
            tracker[word] =1
        else:
            tracker[word] += 1
    return tracker
def report(input):
    new_list = []
    for key in input:
        new_list.append({"char":key,"count":input[key]})
    def sort_on(dict):
        return dict["count"]
    new_list.sort(reverse=True,key=sort_on)
    return new_list

