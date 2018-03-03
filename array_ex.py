# 如果是包含数字的列表，array.array比list要高效

from array import array
from random import random
# 'd'类型码，double
floats = array('d', (random() for i in range(10*7)))
print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10*7)
fp.close()
print(floats2[-1])
print(floats == floats2)

# 数组不支持就地排序list.sort()
# 排序的话使用sorted()函数
# a = array.array(a.typecode, sorted(a))
