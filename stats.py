def get_book_text(filename) :
    with open(filename) as f:
        file_contents = f.read()
    return file_contents

def word_count(string) :
    words = string.split()
    return len(words)

def characters(string) :
    text = string.lower()
    list = []
    for char in text :
        found = False
        for dic in list :
            if dic["name"] == char :
                dic["num"] += 1
                found = True
        if not found :
            list.append({"name": char, "num": 1})
    return list

def sort_on(list) :
    return list["num"]

