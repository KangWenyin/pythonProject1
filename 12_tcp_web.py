import pandas as pd
import numpy as np

data_web=pd.read_csv('data_merge/all/all_weblog.csv',encoding='utf-8')
print(len(data_web))

data_tcp_1=pd.read_csv('data_merge/all/all_tcpLog_week1.csv',encoding='utf-8')
data_tcp_2=pd.read_csv('data_merge/all/all_tcpLog_week2.csv',encoding='utf-8')
data_tcp_3=pd.read_csv('data_merge/all/all_tcpLog_week3.csv',encoding='utf-8')
data_tcp_4=pd.read_csv('data_merge/all/all_tcpLog_week4.csv',encoding='utf-8')
data_tcp_5=pd.read_csv('data_merge/all/all_tcpLog_week5.csv',encoding='utf-8')


data_time=data_web['time']
data_web['stime']=data_time



web_tcp_1=pd.merge(data_web,data_tcp_1,on=['stime','sip','dip','sport','dport'])
#web_tcp_1.to_csv('data_merge/single/web_tcp_1.csv',encoding='utf-8')



web_tcp_2=pd.merge(data_web,data_tcp_2,on=['stime','sip','dip','sport','dport'])
#web_tcp_2.to_csv('data_merge/single/web_tcp_2.csv',encoding='utf-8')

web_tcp_3=pd.merge(data_web,data_tcp_3,on=['stime','sip','dip','sport','dport'])
#web_tcp_3.to_csv('data_merge/single/web_tcp_3.csv',encoding='utf-8')

web_tcp_4=pd.merge(data_web,data_tcp_4,on=['stime','sip','dip','sport','dport'])
#web_tcp_4.to_csv('data_merge/single/web_tcp_4.csv',encoding='utf-8')

web_tcp_5=pd.merge(data_web,data_tcp_5,on=['stime','sip','dip','sport','dport'])
#web_tcp_5.to_csv('data_merge/single/web_tcp_5.csv',encoding='utf-8')


#================================在上述生成的表中添加user_id号====================
user_id=pd.read_csv('data_merge/single/user_id.csv',encoding='utf-8')

web_tcp_user_1=pd.merge(web_tcp_1,user_id,on='sip')
#web_tcp_user_1.to_csv('data_merge/single/web_tcp_user_1.csv',encoding='utf-8')

web_tcp_user_2=pd.merge(web_tcp_2,user_id,on='sip')
web_tcp_user_2.to_csv('data_merge/single/web_tcp_user_2.csv',encoding='utf-8')

web_tcp_user_3=pd.merge(web_tcp_3,user_id,on='sip')
web_tcp_user_3.to_csv('data_merge/single/web_tcp_user_3.csv',encoding='utf-8')

web_tcp_user_4=pd.merge(web_tcp_4,user_id,on='sip')
web_tcp_user_4.to_csv('data_merge/single/web_tcp_user_4.csv',encoding='utf-8')

web_tcp_user_5=pd.merge(web_tcp_5,user_id,on='sip')
web_tcp_user_5.to_csv('data_merge/single/web_tcp_user_5.csv',encoding='utf-8')
