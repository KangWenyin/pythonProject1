import pandas as pd
import re
import os
import numpy as np

financial_id=[1293, 1041, 1431, 1180, 1439, 1186, 1451, 1327, 1467, 1213, 1342, 1346, 1347, 1226, 1108, 1368, 1369, 1370, 1498, 1248, 1124, 1253, 1255, 1137]
financial_id_str = [str(i) for i in financial_id]

#==========================================邮件===========================================
data=pd.read_csv('data_merge/all/all_email.csv',encoding='utf-8')
data1=data.reset_index()

data_from=data1['from']
data_to=data1['to']


label=[]
for i in range(len(data)):
    if data_from[i][0:4] in financial_id_str:  #判断字符串是否在列表中
        label.append(1)
    elif data_to[i][0:4] in financial_id_str:
        label.append(2)
    else:
        label.append(0)

data1['label']=label
for j in range(len(data1)):
    if(data1['label'][j]==0 ):
        data1.drop(j,inplace=True)

data1.to_csv('data_merge/single/financial_email.csv',encoding='utf-8')


