import pandas as pd
import numpy as np
dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df)
# print(df['A'])#打印A列
# print(df.A)#打印A列
# print(df[0:3])#用切片方式打印前三行
# print(df['20130102':'20130104'])
# select by label:loc
#根据标签进行选择
# loc(行,[列])
# print(df.loc['20130102'])
# print(df.loc[:,['A','B']])#打印AB列所有的信息
# print(df.loc['20130102':,['A','B']])#打印AB列20130102及之后所有的信息
# print(df.loc['20130102',['A','B']])#打印AB列20130102的信息
# print(df.loc['20130102':'20130104',['A','B']])#打印AB列20130102到20130104所有的信息

# select by position：iloc
#df.iloc[行，列]
#根据位置进行选择，注意列表起始位为0
# print(df.iloc[3])
# print(df.iloc[3,1])
# print(df.iloc[3:5,1:3])
# print(df.iloc[[1,3,5],1:3])

#mix selection:ix 上面两种方法混合使用
# print(df.ix[:3,['A','C']])

#Boolean indexing  是或者否的筛选
print(df[df.A>8])#只显示A大于8的全部数值

