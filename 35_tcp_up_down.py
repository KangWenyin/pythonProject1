# -*- coding: utf-8 -*-

import pandas as pd

# 读取签到CSV表格数据
dataTcp = pd.read_csv('tcp/all_tcpLog_week5.csv', encoding='utf-8')
# hr用户ID号
stime = dataTcp['stime'].values.tolist()
uplink_length = dataTcp['uplink_length'].values.tolist()
downlink_length = dataTcp['downlink_length'].values.tolist()

stimeList = [s.split(':')[0] for s in stime]
stimeSet = set(stimeList)
stimeSetList = list(stimeSet)
uplink_lengthSum = [0]*len(stimeSetList)
downlink_lengthSum = [0]*len(stimeSetList)

for i in range(len(stime)):
    stimeStr = stime[i].split(':')[0]
    index = stimeSetList.index(stimeStr)
    uplink_lengthSum[index] = uplink_lengthSum[index] + uplink_length[i]
    downlink_lengthSum[index] = downlink_lengthSum[index] + downlink_length[i]

dataTCP = pd.DataFrame()
dataTCP['stime'] = stimeSetList
dataTCP['uplink_lengthSum'] = uplink_lengthSum
dataTCP['downlink_lengthSum'] = downlink_lengthSum
dataTCP.to_csv('tcp/all_tcpLog_week5Sum.csv')

#读取数据
dataTcp1 = pd.read_csv('tcp/all_tcpLog_week1Sum.csv', encoding='utf-8')
dataTcp2 = pd.read_csv('tcp/all_tcpLog_week2Sum.csv', encoding='utf-8')
dataTcp3 = pd.read_csv('tcp/all_tcpLog_week3Sum.csv', encoding='utf-8')
dataTcp4 = pd.read_csv('tcp/all_tcpLog_week4Sum.csv', encoding='utf-8')
dataTcp5 = pd.read_csv('tcp/all_tcpLog_week5Sum.csv', encoding='utf-8')
dataTcp = dataTcp1.append(dataTcp2)
dataTcp = dataTcp.append(dataTcp3)
dataTcp = dataTcp.append(dataTcp4)
dataTcp = dataTcp.append(dataTcp5)
indexs = []
stime = dataTcp['stime'].values.tolist()
astime = []
for s in stime:
    ss = s.split(' ')
    ss2 = ss[0].split('/')
    ss3 = int(ss2[-1]+ss[-1])
    indexs.append(ss3)
    astime.append(s+':00')
dataTcp['index'] = indexs
dataTcp['stime'] = astime
df = dataTcp.sort_values(by="index" , ascending=True)
astime = df['stime'].values.tolist()
auplink_lengthSum = df['uplink_lengthSum'].values.tolist()
adownlink_lengthSum = df['downlink_lengthSum'].values.tolist()
auplink_lengthSumMax = max(auplink_lengthSum)
auplink_lengthSumMin = min(auplink_lengthSum)
adownlink_lengthSumMax = max(adownlink_lengthSum)
adownlink_lengthSumMin = min(adownlink_lengthSum)
    




