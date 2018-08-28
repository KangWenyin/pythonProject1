import pandas as pd
import numpy as np
import re


data=pd.read_csv('data_merge/all/all_email.csv',encoding='utf-8')
data1=data.reset_index() #重新索引
data_sip=data1['sip']
email_from=data1['from']
# data1=data.groupby('sip')
# print(data1.size())

#1.得到sip
sip=[]
for j in range(len(data1)):
    if re.match(r'10.64.106', data_sip[j]):
        # print(email_sip[i])
        sip.append(int(data_sip[j][10:])+6000)
    else:
        if re.match(r'10.64.105', data_sip[j]):
            sip.append(int(data_sip[j][10:])+5000)
        else:
            sip.append(0)
print(sip) #{1:[0,0,235,0,0,7,0],2:[],..30:[]}

#2.得到id
id=[]
for j in range(len(data1)):
    if re.match(r'[0-9]{4}@hightech.com', email_from[j]):

        id.append(int(email_from[j][0:4]))
    else:
        id.append(0)
print(id)

data1['ip']=sip
data1['from_id']=id



for j in range(len(data1)):
    if(data1['ip'][j]==0 or data1['from_id'][j]==0 ):

        data1.drop(j,inplace=True)
    else:
        1==1

data1.to_csv('data_merge/single/email_user.csv',encoding='utf-8')