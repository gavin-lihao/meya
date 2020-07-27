#元组：tuple，不可修改
tuple1=(1,1,2,3,4,5,6,7,8,8)
print(tuple1[2])#访问元组
print(tuple1.count(5))
#元组创建,逗号是关键
temple1=(1,)
print(type(temple1))
#更新、删除
temple2=tuple1[:3]+(10,)+tuple1[4:]#拼接
print(temple2)
#del temple2
#拓展 字符串
str1='i love you'
str2=str1[1:5]
print(str2)

a = 'lihao'
print(a)