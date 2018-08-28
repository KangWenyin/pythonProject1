import pandas as pd

import time
import matplotlib.pyplot as plt

data_web=pd.read_csv('data_merge/all/all_weblog.csv',encoding='utf-8')
print(len(data_web))

user_id=pd.read_csv('data_merge/single/user_id.csv',encoding='utf-8')


web_user=pd.merge(data_web,user_id,on='sip')
web_user.to_csv('data_merge/all/web_user.csv',encoding='utf-8')

