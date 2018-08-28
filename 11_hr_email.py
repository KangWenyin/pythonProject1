import pandas as pd
import re
import os
import numpy as np

hr_id=[1013, 1104, 1110, 1118, 1149, 1165, 1184, 1249, 1251, 1295, 1300, 1312, 1363, 1371, 1378, 1433, 1473, 1499]
hr_id_str = [str(i) for i in hr_id]

#==========================================邮件===========================================
# data=pd.read_csv('data_merge/all/all_email.csv',encoding='utf-8')
# data1=data.reset_index()
#
# data_from=data1['from']
# data_to=data1['to']
#
#
# label=[]
# for i in range(len(data)):
#     if data_from[i][0:4] in hr_id_str:  #判断字符串是否在列表中
#         label.append(1)
#     elif data_to[i][0:4] in hr_id_str:
#         label.append(2)
#     else:
#         label.append(0)
#
# data1['label']=label
# for j in range(len(data1)):
#     if(data1['label'][j]==0 ):
#         data1.drop(j,inplace=True)

#data1.to_csv('data_merge/single/hr_email.csv',encoding='utf-8')


#=================================登录==========================================
data2=pd.read_csv('data_merge/all/all_login.csv',encoding='utf-8',low_memory=False)
data3=data2.reset_index()

data3_user=data2['user']

print(type(data2['user'][7]))  #1175 <class 'str'>

label_2=[]
for i in range(len(data3)):
    if data3_user[i] in hr_id_str:
        label_2.append(1)
    else:
        label_2.append(0)

data3['label']=label_2
for j in range(len(data3)):
    if(data3['label'][j]==0 ):
        data3.drop(j,inplace=True)

data3.to_csv('data_merge/single/hr_login.csv',encoding='utf-8')  #空表,说明hr没有登录过login.csv表


