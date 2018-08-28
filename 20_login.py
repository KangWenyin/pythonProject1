import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

#=============================error=====================================
data=pd.read_csv('data_merge/behavior/login_error.csv',encoding='utf-8')

data1=data.groupby('user')

#print(type(data1.size()))  #<class 'pandas.core.series.Series'>
data2=data1.size()
data3=data2.sort_values()

data11=data.groupby(['user','proto'])
data22=data11.size()
#data3.to_csv('data_merge/behavior/login_error_groupby_num.csv',encoding='utf-8')
#data22.to_csv('data_merge/behavior/login_error_groupby.csv',encoding='utf-8')


#=============================success=====================================
data4=pd.read_csv('data_merge/behavior/login_success.csv',encoding='utf-8')

#以下部分为不合理分类
# data5=data4.groupby(['proto','user'])
# data6=data5.size()
# data6.to_csv('data_merge/behavior/login_success_groupby.csv',encoding='utf-8')

data7=data4.groupby(['user','proto'])
data8=data7.size()
#data8.to_csv('data_merge/behavior/login_success_groupby.csv',encoding='utf-8')
#print(data6)

#================================画图==========================

pd1=pd.read_csv('data_merge/behavior/login_error_groupby.csv',encoding='utf-8')
pd_num=pd1['num'].values  #[2 1 1 ..., 1 1 4]
pd_poto=pd1['user'].values
a=pd_num.tolist()
b=pd_poto.tolist()
c=plt.plot(b,a)
plt.show()
