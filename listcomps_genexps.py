# list comprehension
# 列表推导的作用就是生成列表
# 想生成其他类型的序列，使用生成器表达式

colors = ['black', 'white']
sizes = ['L', 'M', 'S']
tshirts = [(color, size) for color in colors
                         for size in sizes]
print(tshirts)

# 生成器表达式更能够节省内存
# 可以省掉for循环的开销
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

symbols = '#$#%@%'
a = tuple(ord(symbol) for symbol in symbols)
print(a)


import array
b = array.array('I', (ord(symbol) for symbol in symbols))
print(b)
