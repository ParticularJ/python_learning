# list.sort 方法会就地排序列表，不会将原列表复制一份。
# 如果一个函数或者方法对对象进行就地改动那么他就返回None

# sorted 函数，他会新建立一个列表作为返回值

# 两个函数都有两个关键字：1、reverse 、2、 key

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
print(sorted(fruits, reverse=True, key=len))
# sorted 会复制原列表
print(fruits)
fruits.sort()
print(fruits)

# bisect(二分) 模块包含两个函数， bisect 和 insort
# 都利用二分法来在有序序列中查找或插入元素

# bisect(a, b) 在a中搜索b的位置,index
# 使用a.insert(index, b),在位置index中插入b
# 或者直接使用insort(a,b)


# bisect函数有两个可选参数 ——lo，和hi——
# bisect函数其实是bisect_right函数，还有一个bisect_left函数
# 区别是bisect_left函数返回的插入位置是原序列中和被插入位置相等的元素的位置
# 即bisect_left插入元素的前面，而right插入后面
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23 , 26, 29 ,30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<3d}'

def demo(bisec_fn):
    for needle in reversed(NEEDLES):
        position = bisec_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':

    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

# 一个简单的成绩与分数的对应

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i=bisect.bisect(breakpoints, score)
    return grades[i]

print([grade(score) for score in [33, 99, 77, 80, 89, 90, 100]])


# inort(seq, item)将item插入到seq中并且不改变seq的顺序

import random

SIZE = 7
random.seed(172)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
