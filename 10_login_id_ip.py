import pandas as pd
import numpy as np
import re


data=pd.read_csv('data_merge/all/all_login.csv',encoding='utf-8')
data1=data.reset_index(drop=True)

data_sip=data1['sip']
data_user=data1['user']
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
print(sip)

# #2.得到id
# id=[]
# for j in range(len(data1)):
#     if re.match(r'[0-9]{4}@hightech.com', data_user[j]):
#
#         id.append(int(email_from[j][0:4]))
#     else:
#         id.append(0)
# print(id)
#
# data1['ip']=sip
# data1['from_id']=id



for j in range(len(data1)):
    if(data1['ip'][j]==0 ):

        data1.drop(j,inplace=True)
    else:
        1==1

data1.to_csv('data_merge/single/login_ip_user.csv',encoding='utf-8')