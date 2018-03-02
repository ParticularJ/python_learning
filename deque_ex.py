# collections.deque类是一个线程安全、可以快速从两端添加或者删除
# 元素的数据类型。可以存放最近用到的几个元素。

from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)

# rotate函数接受参数n,当n>0,队列最有变的n个元素被移动到队列的左边
# 当n<0s时，最左边的n个元素移动到右边
dq.rotate(3)
print(dq)

dq.rotate(-4)
print(dq)

dq.appendleft(-1)
print(dq)

dq.extend([11, 22, 33])
print(dq)
# extendleft(iter)会把迭代器里的元素逐个添加到双向队列的左边
# 因此迭代器里的元素会逆序出现在队列里
dq.extendleft([10, 20, 30, 40])
print(dq)
