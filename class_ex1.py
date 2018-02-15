import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with parameters @@@",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    #print(len(sys.argv))
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding = 'UTF-8'))

def convert(snippet, phrase):
    # capitalize使得第一个字符为大写，其余为小写
    # random.sample(sequence, k)  从指定序列中随机获取k个元素作为一个片段返回
    # sample函数不会修改原有序列
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        # 随机生成1，2，3
        param_count = random.randint(1, 3)
        # 将生成的参数以"par1,par2，"添加到list
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        #  Python way of copying a list
        print(f"the sentence is : {sentence}")
        result = sentence[:]

        # fake class names
        for word in class_names:
            # str.replace(old, new, max)，replace old with new ,no more than max
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake paremeter list
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)
    return results

# keep going util they hit
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye.")
