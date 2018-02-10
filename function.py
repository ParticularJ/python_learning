def break_words(stuff):
    # break words for us
    # split(str='',num=?)通过指定分隔符对字符串进行切片
    #如果参数num 有指定值，则仅分隔 num 个子字符串
    words = stuff.split(' ')
    return words

def sort_words(words):
    # sorted()可对所有可迭代对象排序
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    print(word)

def print_last_word(words):
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
