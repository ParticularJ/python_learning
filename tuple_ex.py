# 元组其实是对数据的记录，元组中的每个元素都存放了
# 记录中一个字段的数据，外加这个字段的位置
# 如果我们在元组内对元素排序，这些元素所携带的信息会丢失

lax_coordinates  = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
                ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# _占位符能帮助我们排除我们不需要的参数返回值
for country, _ in traveler_ids:
    print(country)

# 在拆包中，我们也可以使用“*”
# 用 * 来表示剩余的元素

a, b, *rest = range(1, 5)
print("a={},b={},*rest={}{}".format(a, b, *rest))

# 接受表达式的元组可以是嵌套式的
# 比如（a, b, (c, d)）

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ("Delhi", 'IN', 21.31, (28.613889, 77.208889)),
    ("Mexico City", 'MX', 20.142, (19.433333, -99.13333333)),
    ('New Yourk', 'US', 20.104, (40.8022382, -74.0203123)),
    ('Sao Paulo', 'BR', 19.23, (-23.5323,-46.2143214))
]

# :15空14格， ^ 剧中
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'

for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
