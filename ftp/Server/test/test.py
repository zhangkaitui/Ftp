# -*- coding: utf-8 -*-
# Date: 2019/1/29


import shelve

# f = shelve.open('test')
# f['oldboy'] = {'name': 'oldboy'}
# print(f['oldboy'])  # {'name': 'oldboy'}
# f['oldboy'].update({'age': 84})
# print(f['oldboy'])  # {'name': 'oldboy', 'age': 84}
# f.close()


# f = shelve.open('test')
# f['oldboy'] = {'name': 'oldboy'}
# print(f['oldboy'])  # {'name': 'oldboy'}
# temp_dict = f['oldboy']
# temp_dict.update({'age': 84})
# f['oldboy'] = temp_dict
# print(f['oldboy'])  # {'name': 'oldboy', 'age': 84}
# f.close()

# f = shelve.open('test')
# print('oldboy' in f.keys())  # KeysView(<shelve.DbfilenameShelf object at 0x00BDEA10>)
# print(list(f.keys()))  # ['oldboy']
# f.close()


# f = shelve.open('test')
# class A: pass
# a = A()
# f['l'] = [1, 2, 3]
# f['t'] = (1, 2, 3)
# f['d'] = {'张开': '帅帅帅', '自恋狂': '抠脚！'}
# f['se'] = {1, 2, 3}
# f['st'] = '张开666'
# f['obj'] = a
# print(f['l'])  # [1, 2, 3]
# print(f['t'])  # (1, 2, 3)
# print(f['d'])  # {'张开': '帅帅帅', '自恋狂': '抠脚！'}
# print(f['se'])  # {1, 2, 3}
# print(f['st'])  # 张开666
# print(f['obj'])  # <__main__.A object at 0x031E9510>
# f.close()

# f = shelve.open('test', writeback=True)

# f.sync()




# with shelve.open('test', writeback=True) as f:
#     f['zhangkai'] = 666
#     print(f.get('zhangkai'))  # 666
#     del f['zhangkai']
#     print(f.get('zhangkai'))  # None



# with shelve.open('test', writeback=True) as f:
#     f['zhangkai'] = 666
#     f['zhangkai'] = 888
#     print(f.get('zhangkai'))  # 888

# with shelve.open('test') as f:
#     f['zhangkai'] = 666
#     print(f['zhangkai'])  # 666
#     temp = f['zhangkai']
#     temp = 888
#     f['zhangkai'] = temp
#     print(f.get('zhangkai'))  # 888




# with shelve.open('test') as f:
#     f['zhangkai'] = 666
#     print(f['zhangkai'])  # 666
#     print(f['zhangkai1'])  # KeyError: b'zhangkai1'
#     print(f.get('zhangkai'))  # 888
#     print(list(f.keys()))  # ['oldboy', 'l', 't', 'd', 'se', 'st', 'obj', 'zhangkai']






d = shelve.open('test', writeback=True)

# 增
class Person: pass
oldboy = Person()
d['obj'] = oldboy
d['l'] = [1, 2, 3]
d['t'] = (1, 2, 3)
d['d'] = {'a': 1}
d['se'] = {1, 2, 3}
d['st'] = 'abc'

# 查，直接查询
print(d['obj'])  # <__main__.Person object at 0x03006570>
print(d['l'])  # [1, 2, 3]
print(d['t'])  # (1, 2, 3)
print(d['d'])  # {'a': 1}
print(d['se'])  # {1, 2, 3}
print(d['st'])  # abc
# 查，get方式
print(d.get('obj'))  # <__main__.Person object at 0x03006570>
# 查所有的key
print(list(d.keys()))  # ['oldboy', 'l', 't', 'd', 'se', 'st', 'obj', 'zhangkai']

# 改,当writeback=True时可以直接修改
d['l'] = ['a', 'b', 'c']
print(d['l'])  # ['a', 'b', 'c']
# 改，当writeback=False的时候，需要显式的修改
temp = d['t']
temp = ('x', 'y', 'z')
d['t'] = temp
print(d['t'])  # ('x', 'y', 'z')

# 删
del d['se']
print(list(d.keys()))  # ['oldboy', 'l', 't', 'd', 'st', 'obj', 'zhangkai']

d.close()



