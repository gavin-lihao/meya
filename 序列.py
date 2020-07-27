#列表、元组、字符串统称为序列
#方法
a=(1,2,3,4,5,78,-9,0)
b='hello world'
c=[90,'a','b',[78,80,-1]]
print(list(a))#list->转成列表
print(len(c))#len->查询长度
print(max(a))#max->返回最大值，参数类型要统一
print(min(a))#max->返回最小值 ，参数类型要统一
print(sum(a))#sum->求和
print(sorted(a))#sorted->排序
print(reversed(a))#reversed->翻转
print(list(reversed(a)))#reversed->翻转,强制转换成list
print(enumerate(a))#enumerate->枚举
print(list(enumerate(a)))#enumerate->枚举，强制转换成list
print(zip(a,b))#zip->成对打包
print(list(zip(a,b)))#zip->成对打包，强制转换成list
