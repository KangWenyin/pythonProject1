import pandas as pd

data=pd.read_csv('data_merge/single/hr_table.csv',encoding='utf-8')
data1=data.groupby('from_new')
print(data1)
user_num=data1.size() #<class 'pandas.core.series.Series'>
#user_num.to_csv('data_merge/single/hr_table_groupby.csv',encoding='utf-8')

a=pd.read_csv('data_merge/single/hr_table_groupby.csv',encoding='utf-8')

a_num=a['num']
hr_error=[]
hr_id=[]
for i in range(len(a_num)):
    if a_num[i]<10:
        hr_error.append(a['id'][i])
    else:
        hr_id.append(a['id'][i])
print(hr_id)
print(len(hr_id)) #18个，原来有45个

