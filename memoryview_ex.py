# memoryview 是一个内置类，能让用户在不复制内容的情况下
# 操作同一个数组的不同切片
# memoryview.cast的概念跟数组模块类似，能用不同的方式读写同一
# 块内存数据，而且内容字节不会随意移动。

import array
# h:signed short
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])

# 转成unsigned char
memv_oct = memv.cast('B')
print(memv_oct.tolist())
# 一个整数占两个字节，将高位变成4，则得到“0000 0000 0000 0100”
memv_oct[5] = 4
print(numbers)
