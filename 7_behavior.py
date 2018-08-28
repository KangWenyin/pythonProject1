import pandas as pd
import re

data=pd.read_csv('data_merge/all/all_tcpLog.csv',encoding='utf-8')
data_sip=data['sip']
# data1=data.groupby('sip')
# print(data1.size())

sip=[]
for j in range(len(data)):
    if re.match(r'10.64.106', data['sip'][j]):
        # print(email_sip[i])
        sip.append(int(data['sip'][j][10:])+6000)
    else:
        if re.match(r'10.64.105', data['sip'][j]):
            sip.append(int(data['sip'][j][10:])+5000)
        else:
            sip.append(0)
print(sip) #{1:[0,0,235,0,0,7,0],2:[],..30:[]}

data['ip']=sip

for j in range(len(data)):
    if(data['ip'][j]==0 ):

        data.drop(j,inplace=True)
    else:
        1==1

data.to_csv('data_merge/single/all_tcpLog.csv',encoding='utf-8')