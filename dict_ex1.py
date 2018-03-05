# 字典的变种
# collections.OrderedDict,在添加键的时候保持顺序
# collections.ChainMap,可容纳数个不同的映射对象，
# 进行查找时，这些对象被当作一个整体被逐个查找。
# collections.Counter,计数器，更新键时增加
# most_common([n])按照次序返回最常见的n个键

import collections

ct = collections.Counter('abracadabra')
print(ct)

# update首先检查元素有没有key，有的话正常，没有的话，转化为（key, value）
ct.update('aaaaazzz')
print(ct)

print(ct.most_common(2))

# collections.UserDict,创造自定义映射类型，以userdict为基类

class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    # 将所有存储的键变为字符串
    def __setitem__(self, key, item):
        self.data[str(key)] = item

a = StrKeyDict([('1', 'one'), ('2','two')])
print(a[1], a.get('1'))
a[1] = 'three'
print(a)

# 标准库里所有的映射类型都是可变的，但有时候我们需要让之不可变
# MappingProxyType，返回只读的映射视图,并且他是动态的，我们在原映射改变
# 可以通过视图观察到

from types import MappingProxyType
d = {1:'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
# 使用d_porxy[1]=x,typeerror
d[2] = 'B'
print(d_proxy)



# 集合的本质是许多唯一对象的聚集，因此，集合可以用于去重
# 集合的元素必须是可散列,如果建立空集，必须使用set()

# 可散列对象
# 1、支持hash（）,并且通过__hash__（）方法得到的散列值是不变的
# 2、支持通过__eq__()方法来检测相等性；3、若a == b为真，则hash(a)==hash(b)
# 所有由用户自定义的对象默认都是可散列的。
# 字典使用了散列，而散列表稀疏的特性使得在存放巨大的记录的字典效率低。
# 使用元组或者具名元组构成的列表是很好的选择，只是在空间优化的层面
# 如果有足够的内存，可以忽略。因为，键查询非常块，
