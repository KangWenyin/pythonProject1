import pandas as pd

import time
import matplotlib.pyplot as plt

data1=pd.read_csv('data_merge/all/all_checking.csv',encoding='utf-8')
#data1=data.groupby('id').size()
data_id=data1['id'].unique()
for i in data_id:
    dataId = data1[data1['id'].isin([i])]
    print(dataId)
    dataId.to_csv('data_merge/all/people_checking.csv',encoding='utf-8')
