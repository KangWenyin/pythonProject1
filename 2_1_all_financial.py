import pandas as pd
import re
import os
import numpy as np

data=pd.read_csv('data_merge/all/all_email.csv',encoding='utf-8')
email_subject=data['subject']
all=[]
#print(email_subject)
#
#1 得到主题是financial关键字的人
email_count=[]
for j in range(len(email_subject)):
    if re.match(r'(财务分析|会计核算|税务|资金)', email_subject[j]):
        # print(email_sip[i])
        email_count.append(1)
    else:
        email_count.append(0)
print(email_count) #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
data['financial']=email_count
#print(data.columns)


#2.将是0的行删除，得到financial的列表

for j in range(len(data)):
    if(data['financial'][j]==0 ):
        #print(data[i-1]['from_new'][j])
        data.drop(j,inplace=True)

# 3. 重新索引并得到from的id
all=[] #所有邮件的列表id
data_index_new=data.reset_index(drop=True)

from_new = []
for j in range(len(data_index_new)):
    from_new.append(int(data_index_new['from'][j][0:4]))

data_index_new['from_new'] = from_new
#data_index_new.to_csv('data_merge/single/financial_table_2.csv', encoding='utf-8')

#3.1 筛选 得到主题是financial关键字的to的人
for j in range(len(data_index_new)):
    all.append(re.findall(r'[0-9]{4}',data_index_new['to'][j]))
print(all)  #[['1041', '1368', '1347', '1255', '1248', '1327',



#3.2  筛选 得到主题是financial关键字的from的人
email_from=data_index_new['from']

for j in range(len(email_from)):
    if re.match(r'(财务分析|会计核算|税务|资金)',email_from[j]):

        all.append(email_from[j][0:4])
    else:
        1==1

#3.3 筛选 从email_subject得到‘报销’的to 的id
# for i in range(len(email_subject)):
#     if re.match(r'(报销)',email_subject[i]):
#         all.append(data['to'][i][0:4])
#     else:
#         1==1
# print(all)

#4. 处理嵌套列表
def flat(all):
    for k in all:
        if not isinstance(k, (list, tuple)):
            yield k
        else:
            yield from flat(k)
b=list(flat(all))
print(b)

for i in range(len(b)):
    b[i]=int(b[i])
print(1,len(b),b)

c=list(set(b)) #得到financial的id
print(2,len(c),c)
financial_id=pd.Series(c)
print(3,len(financial_id.unique()),financial_id.unique())

financial_id.to_csv('data_merge/single/financial_id.csv',encoding='utf-8') #共24人
