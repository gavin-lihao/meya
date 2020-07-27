# def funct_1():
#     print('函数')
# funct_1()
#
# def funct_2(name):#形参
#     print(name+'我爱你')
# funct_2('python')#实参
#
# def funct_3(num1,num2):
#     print(num1+num2)
# funct_3(2,3)
# 函数返回值
# def funct_3(num1,num2):
#     return (num1+num2)
# print(funct_3(2,3))
# 函数文档
# def funct_4(num1,num2):
#     '求两者之积'#函数文档
#     return (num1*num2)
# print(funct_4(5,6))
# print(funct_4.__doc__)#显示函数文档
# print(help(funct_4))
# # print(funct_4(num1,num2))#显示函数文档
# #关键字参数，为了顺序正确
# def funct_5(name,word):
#     print(name+'说过：'+word)
# funct_5(word='python是万能的',name='xx')
# #默认参数，给形参赋初值
# def funct_5(name='XX',word='python是万能的'):
#     print(name+'说过：'+word)
# funct_5()
# funct_5(word='我爱你',name='李皓')
# 搜集参数，在创建函数初不确定有几个形参
def funct_6(*nums):
    print('参数的长度是：', len(nums))
    print('第二个参数是：', nums[1])


funct_6(1, 'python', 'hello world', 4)  # 元组打包


# 过程
# 变量的作用域
# 局部变量&全局变量，在函数内部最好不要修改全局变量
# def funct_7(price, rate):
#     final_price = price * rate
#     return final_price
#
#
# old_price = float(input('请输入原价：'))
# old_rate = float(input('请输入折扣率：'))
# new_price = funct_7(old_price, old_rate)
# print('打折后的价钱：', new_price)

#强行在函数内修改全部变量，关键字->global()
count=10
print(count)
def count():
    global count
    count=5
    print(count)
count()
print(count)
#内嵌函数

def fun1():
    print('fun1()正在被调用...')
    def fun2():
        print('fun2()正在被调用...')
    fun2()
fun1()

#闭包
def funx(x):
    def funy(y):
        return x*y
    return funy
i=funx(8)
print(i(5))
print(funx(8)(5))

#关键字->nonlocal()

def fun66():
    x=5
    def fun77():
        nonlocal x
        x*=x
        return x
    return fun77()
print(fun66())
