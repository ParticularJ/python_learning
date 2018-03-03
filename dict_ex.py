# 标准库里的所有映射类型都是利用dict来实现的，因此有个共同限制
# 只有可散列的数据类型才能用作这些映射里的键
# 可散列数据类型：在这个对象的生命周期中，它的散列值不变，并且，
# 这个对象需要实现__hash__()方法，并且散列对象还要有__qe__()方法跟其他键比较
# 原子不可变数据类型（str, bytes和数值类型）都是可散列类型，frozenset也是可散列
# 只有元组中包含的元素都是可散列，元组才是可散列类型

# 用setdefault处理找不到的键
import collections
import sys
# 正则表达式是一个特殊的字符序列，方便检查一个字符串是否与某种模式匹配
import re
# 根据一个模式字符串和可选的标志参数生成一个正则表达式对象
# compile确定匹配模式
WORD_RE = re.compile(r'\w+')

index = {}
# 使用defaultdict
index1 = collections.defaultdict(list)



with open(sys.argv[1], encoding='utf-8') as fp:
    # 将可遍历的对象组合为一个索引序列，同时列出数据和数据下标
    # 1表示下表起始位置
    for line_no, line in enumerate(fp, 1):
        print(line_no, line)
        # 找到正则式匹配的字符串，并把他作为迭代器返回
        for match in WORD_RE.finditer(line):
            # 匹配就返回真个字符串
            word = match.group()
            # 开始匹配的位置
            print(match.start())
            column_no = match.start()+1
            location = (line_no, column_no)
            # 使用get的方法
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences
            # 使用setdefault方法
            index.setdefault(word, []).append(location)
            # 使用defaultdict
            index1[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])

for word in sorted(index1, key=str.lower):
    print(word, index1[word])

# 单纯的查找取值
# defaultdict: 处理找不到的键的一个选择
# 如： dd = defaultdict(list)
# 如果键值‘new-key’在dd中不存在的话，表达式会按照以下步骤来行事
# 调用list（）创建一个新列表，把‘new-key’作为键

print("-------------**************-------------------------")
# __missing__,该方法只会被__getitem__调用，即d[k]
class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

def __contains__(self, key):
    return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'], d[4])
print(d.get('2'), d.get(4))

print(2 in d)
