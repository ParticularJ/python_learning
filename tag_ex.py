# 调用函数时使用 * 和 ** 展开可迭代对象，映射到单个参数

# 定义函数时，若想指定仅限关键字参数，要把它们放到前面有*的参数后面
# 如果不想支持数量不定的定位参数，但是想支持仅限关键字参数，在签名中放入一个*

# 使用cls关键字参数传入“class”属性
def tag(name, *content, cls=None, **attrs):
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                            for attr, value
                            in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                        (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

print(tag('br'))
# 第一个参数后面的任意参数会被content捕获
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
# 没有明确指定名称的关键字会被**attrs捕获，存入字典
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', cls='sidebar'))
# content指定参数他会通过attrs捕获，不能直接给*content赋值
print(tag(content='testing', name="img"))
print(tag(name='ing', content='123'))
my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
            'src': 'sunset.jpg', 'cls': 'framed'}
# 在my_tag前面加上 **,字典中的所有元素作为单个参数传入
print(tag(**my_tag))
