#拓展 字符串
str1='i love you'
str2=str1[1:5]
print(str2)
str3='I LOVE YOU TOO'
#字符串方法
print(str1.capitalize())#第一个字符大写
print(str3.casefold())#将所有字符转成小写
print(str3.center(48))#居中
print(str3.count('O'))#计数
# 小甲鱼论坛
#格式化
# 字符串格式化--关键字参数/位置参数
print('{0} love {1}'.format('i','you'))#位置参数
print('{a} love {b}'.format(a='i',b='you'))#关键字参数
print('{0} love {b}'.format('i',b='you'))#关键字和位置参数混用，位置参数必须在关键字之前使用
#转义
print('\ta')#tab
print('\\')
print('{{0}}'.format('不打印'))
print('{0:.1f}{1}'.format(123.456,'GB'))

#小甲鱼论坛
print('%c'%97)#格式化字符及其ASCII码
print('%c %c %c '%(97,98,99))#多字符用元组圈起来
print('%s'%'i love you')#格式化字符串
print('%d+%d=%d'%(4+5,5+6,4+5+5+6))#格式化整数
print('%o'%10)#格式化无符号八进制数
print('%x'%10)#格式化无符号十六进制
print('%X'%10)#格式化无符号十六进制
print('%f'%10.5678)#格式化定点数，可指定小数点后的精度，默认六位小数
print('%e'%10.5678)#用科学计数法格式化定点数，%E也是同样作用
print('%g'%10.5678)#只能选择用%f或者%e，%G同样作用

#格式化

print('%5.1f'%10.5678)#m.n->m是显示的最小总宽度，n是小数点后的位数，四舍五入
print('%-10d'%10.5678)#左对齐
print('%+d'%-10.5678)#在整数面前显示+
print('%#x'%10)#在八进制数前面显示0，在16进制显示0x或者0X
print('%010d'%10)#显示的数字前面填充0取代空格
