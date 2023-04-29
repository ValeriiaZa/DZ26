import string

def first_word(text):
    lst = []
    for i in text:
        if i in string.punctuation + ' ' and len(lst) == 0:
            pass
        elif i in string.punctuation + ' ' and i != "'" and len(lst) != 0:
            break
        else:
            lst.append(i)
    str_str = "".join(lst)
    print(str_str)
    return str_str


str1 = 'Hello world'
first_word(str1)
