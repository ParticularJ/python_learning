# 具名元组
# collections.namedtuple是一个工厂函数，可以构建
# 一个带字段名的元组和一个有名字的类

from collections import namedtuple
City = namedtuple('City', 'name country population coordinate')
tokyo = City('Tokyo', 'JP', 34.535253, (32,12))

# _fields属性包含这个类所有字段名称的元组
print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.983, LatLong(26.232,66.2321312))

# _make()通过接受一个可迭代对象来生成类的实例
# 作用和City(*delhi_data)一致
delhi = City._make(delhi_data)

#_asdict()把具名元组以collections.OrderedDict形式返回
delhi._asdict()

for key, value in delhi._asdict().items():
    print(key + ':', value)
