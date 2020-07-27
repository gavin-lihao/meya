#非递归版本
x=input('输入一个正整数用来求它的阶乘:')
x=int(x)
mulp=1
for i in range(1,x+1):
    mulp*=i
print(mulp)
#递归版本(1.有重复调用自身的行为，2.有一个返回条件，避免死循环)
def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
number=int(input('输入一个正整数用来求它的阶乘:'))
result=factorial(number)
print('%d 的阶乘是：%d'%(number,result))
