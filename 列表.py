# fa='fishec'
# for i in fa:
#     print(i,end='')
# number=['11','222','33']
# for each in number:
# #     print(each,len(each))
# # print(range(3))
# # print(list (range(3,10,2)))
# # for i in range(10):
# #     if i%2!=0:
# #         continue
# #         print(i)
# #     print(i)
# #列表list
# mix=['xiao',1,[1,2,3]]#可以包含不同类型
# print(mix)
# #参数添加
# mix.append('葫芦娃')#只能加一个参数，可以添加列表，当做一个参数
# print(mix,len(mix))
# mix.extend(['大娃','二娃'])#可以添加列表，列表中有多个参数,融入大列表中
# print(mix,len(mix))
# mix.insert(0,'狐狸精')
# print(mix,len(mix))
# print(mix[0])
# #位置交换
# temp=mix[0]
# mix[0]=mix[1]
# mix[1]=temp
# print(mix,len(mix))
# #参数删除
# mix.remove('狐狸精')#参数必须在列表中，否则报错
# print(mix,len(mix))
# del mix[1]
# print(mix,len(mix))
# # del mix  把整个列表删掉，非清空列表
# # print(mix,len(mix))
# # print(mix.pop(),len(mix))#pop有返回值，默认删掉最后一个参数
# print(mix.pop(1))
# print(mix,len(mix))
# #列表分片
# print(mix[1:3])#列表拷贝，原列表依然存在
# mix2=mix
# print(mix2)
# mix2=mix[:]
# print(mix2)
#列表拼接
list1=[123,456,789,'大娃',['蝎子精','蛇精']]
list2=[456,789,890]
list=list1+list2#同字符串拼接，只适用于拼接已存在的元素，无法添加新元素
print(list,len(list))
#列表复制
list*=3
print(list,len(list))
#列表包含判断
print('大娃'in list)
print('蝎子精'in list)#返回值：False
print('蝎子精'in list[4])#返回值：True
print( list[4][1])#返回值：蛇精
#列表常用方法
print(dir(list))#dir->列举
#['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
# '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
# 'reverse', 'sort']
print(list.count('蝎子精'))#计数
print(list.index(123))#查找位置，参数第一次出现的位置
print(list.index(123,4,9))#查找位置，在指定范围内参数第一次出现的位置
print(list2)
#reverse只是操作list，不是创建一个新的列表
list2.reverse()
print(list2)#列表翻转，没有返回值
list3=[4,6,3,2,6,5,4,8,9]
#排序
list3.sort()
print(list3)#排序，默认从小到大
#sort(func,key,reverse=False)默认是False->从小到大排序
list3.sort(reverse=True)
print(list3)#排序,从大到小

#拷贝
list4=list3
list5=list3[:]
#以上虽然都得到一个相同的列表，但是有不同
#list4是将指针指向list3，list3改变，list4也改变
#list5是拷贝list3，list3改变，list5不改变
list3.sort()
print('list3是：',list3)
print('list4是：',list4)
print('list5是：',list5)




