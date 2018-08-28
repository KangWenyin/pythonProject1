import pandas as pd
import re
import os
import numpy as np
#============================30张表格的数据======================================
data=pd.read_csv('data_merge/all/all_email.csv',encoding='utf-8')
email_sip=data['sip']
email_from=data['from']


#2.1 匹配正则表达式
email_count = [] #sip
email_count2=[]  #from

for j in range(len(email_sip)):
    if re.match(r'10.64.106', email_sip[j]):
        # print(email_sip[i])
        email_count.append(int(email_sip[j][10:]))
    else:
        email_count.append(0)
print(email_count) #{1:[0,0,235,0,0,7,0],2:[],..30:[]}

#2.2 匹配正则表达式
for j in range(len(email_sip)):
    if re.match(r'[0-9]{4}@hightech.com', email_from[j]):
        # print(email_sip[i])
        email_count2.append(int(email_from[j][0:4]))
    else:
        email_count2.append(0)
print(email_count2)

#3. 将sip和from的员工写入Email.csv文件
data['sip_new']=email_count
data['from_new'] = email_count2
print(data.columns) #Index(['time', 'proto', 'sip', ..'subject', 'sip_new'], dtype='object')

#4.将两者中只要有一个是0的行删除，得到hr的列表
hr_list=[]
for j in range(len(data)):
    if(data['sip_new'][j]==0 or data['from_new'][j]==0):
        #print(data[i-1]['from_new'][j])
        data.drop(j,inplace=True)
print(data)


num_hr=data['sip_new'].unique()
#print(num_hr)
print(len(num_hr)) #35个

hr_id=data['from_new'].unique() #hr的id号
print(hr_id)
print(len(hr_id)) #35个

#此id为没有处理过的id
pd_hr_id=pd.Series(hr_id)


#=======================在hr_email.csv表中找‘to乱码’和to中包含‘1013的id’===============================
#1.
data_index_new=data.reset_index(drop=True)
#print(data_index_new)
hr_true=[]
for i in range(len(data_index_new)):
    if re.match(r'(1013@hightech.com|1013@hightech.com;[0-9]{4}@hightech.com)',data_index_new['to'][i]):
        hr_true.append(1)
    else:
        if re.match(r'[0-9]{4}@hightech.com',data_index_new['to'][i]):
            hr_true.append(0)
        else:
            hr_true.append(1)


data_index_new['financial_true']=hr_true
for j in range(len(data_index_new)):
    if(data_index_new['financial_true'][j]==0 ):
        data_index_new.drop(j,inplace=True)
print(data_index_new)
data_index_new.to_csv('data_merge/single/hr_table.csv',encoding='utf-8')

