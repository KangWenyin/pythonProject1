from datetime import datetime
# a=datetime.now()
# print(a)
# print(a.year,a.month,a.day)
#
# b=datetime(2018,4,23)-datetime(2018,4,20,10,0)
# print(b)
# print(b.days)
# print(b.seconds)

#字符串的转化
a=datetime(2018,3,4)
print(a)
print(str(a))

value='2018-05-24'
a1=datetime.strptime(value,'%Y-%m-%d')  #按照格式将字符串转化为日期
print(a1)

from dateutil.parser import parse
a2=parse('2011/1/3') #parse几乎可以解析所有人类可以理解的日期形式
print(a2)


#=====================================================import pandas as pd======================================
import pandas as pd
import numpy as np
a3=['2011/1/4 10:45','2011/1/3']
a4=pd.to_datetime(a3)
print(1,a4)

# data=pd.read_csv('data_merge/all/all_login.csv')
# checkin=data['checkin']

dates=[datetime(2018,5,21),datetime(2018,5,22),datetime(2018,5,23),datetime(2018,5,24),datetime(2018,5,25),datetime(2018,5,26)]
ts=pd.Series(np.random.randn(6),dates)
print(ts)
print(type(ts))
print(ts.index)
print(ts.index[0])
a5=ts.index[0]
a6=ts[a5]
print(6,a6)
# a7=ts['20180521'] 不可行
# a8=ts[a7]
# print(8,a8)
#
longer_ts=pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
#print(longer_ts)

a9=ts[datetime(2018,5,23):]
print(9,a9)
a10=ts[]





