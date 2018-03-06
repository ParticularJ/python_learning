# 一等函数：1、在运行时创建；2、能赋值给变量或数据结构中的元素；
# 3、能作为参数传给函数；4、能作为函数的返回结果
# all(iterable),如果每个元素都是真值，返回True。
# any(iterable),只要有真值就返回true

# 匿名函数，lambda关键字 创建匿名函数，并且只能使用纯表达式
# 生成器函数，使用yield关键字的函数或方法

import random

class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()

bingo = BingoCage(range(3))
print(bingo.pick())
# 因为实现了__call__函数，所以可以直接使用bingo()
print(bingo())
print(callable(bingo))
