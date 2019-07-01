import numpy as np
import pandas as pd
from pandas import DataFrame as df

np.str_
print('--------------Series--------------')
s = pd.Series([1,3,5,np.nan,6,8,'ab'])
s = s * 2
print(s)
print(s.index)
print(s.values)
print(s.values[0],',',s.values[6])
print(s.isnull())
print('--------------DataFrame---二维的Series-----------')
data = {"name":['google','baidu','yahoo'],"marks":[100,200,300],"price":[1,2,3]}
f = df(data)
print(f)
print(f.index)
print(f.values)
print(f.values[0],',',f.values[2])
print(f.values[0][0],',',f.values[2][2])

print('--------------DataFrame---二维的Series-----------')
f2 = df(data,columns=['name','marks','price'],index=['a','b','c'])
print(f2)