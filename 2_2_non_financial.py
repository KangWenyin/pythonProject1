import pandas as pd
import numpy as np
import re


#=====================all_email__1.csv'表示财务报账和报销的to的人数，共198=======================
data=pd.read_csv('data_merge/all/all_email.csv',encoding='utf-8')
all=[]
email_subject=data['subject']
for i in range(len(email_subject)):
    if re.match(r'财务报账|报销',email_subject[i]):
        all.append(data['to'][i][0:4])

    else:
        data.drop(i, inplace=True)

print(all)  #['1291', '1231', '1297', '1248', '1253', '1124', '1368', '1397', '1439',
data_index_new=data.reset_index(drop=True)
data_index_new.to_csv('data_merge/all/all_email__1.csv',encoding='utf-8')

print(len(data_index_new['to'].unique()))  #198
