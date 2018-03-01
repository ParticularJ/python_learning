# 省略（ellipsis）,用法为（...）
# f(a, ..., z),若x是4维，那么x[i,...]就等于x[i,:,:,:]

l = list(range(10))
print(l)

l[2:5] = [20, 30]
print(l)

del l[5:7]
print(l)

l[3::2] = [11, 22]
# 不能这样赋值 l[2:5] = 100
# 切片的右侧必须为可迭代的序列

l[2:5] = [100]
print(l)

# 对序列使用 + 和 * ，其中+号表示拼接，*表示复制
# 如果a*n，序列a里的元素是对其他可变对象的引用的话
# my_list = [[]]*3,其实得到的三个元素是三个引用，
# 这三个引用都指向同一个列表。




# 建立由列表组成的列表，即初始化一个嵌套几个列表的列表

board = [['_']*3 for i in range(3)]
print(board)

board[1][2] = 'X'
print(board)

# 外面的列表其实包含了3个指向同一个列表的引用
board = [['_']*3]*3
print(board)
board[1][2] = 'X'
print(board)


# 追加同一个对象3次到board

row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
board[2][2] = 'C'
print(board)

# 分别建立新的列表到board
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
board[1][2] = 'Z'
print(board)
