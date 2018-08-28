import pandas as pd
checking = pd.read_csv('tiao.csv', encoding='gbk')
host=checking['host']
#print(host)
grouped=checking.groupby('host')
print(grouped)
user_num=grouped.size()
print(user_num)
print(len(user_num))

sip=checking['sip']
#print(host)
groupesip=checking.groupby('sip')
print(groupesip)
sip_num=groupesip.size()
print(sip_num)
print(len(sip_num))