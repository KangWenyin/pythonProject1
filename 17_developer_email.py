import pandas as pd
import re
import os
import numpy as np


#==========================================developer邮件记录===========================================

# # #得到开发的人员，共256个
# data1=pd.read_csv('data_merge/all/all_login.csv',encoding='utf-8',low_memory=False)
# user=data1['user'].unique()
#
# # print(user)
# # print(len(user)) #257
# user1=np.delete(user,0)
# user1=user1.tolist()
# # print(user1)
# # print(len(user1)) #256
# user2=pd.DataFrame(user1)
# #user2.to_csv('data_merge/single/developer_id.csv',encoding='utf-8')
#
#
# data=pd.read_csv('data_merge/all/all_email.csv',encoding='utf-8')
# data2=data.reset_index()
#
# data_from=data2['from']
# data_to=data2['to']
#
#
# label=[]
# for i in range(len(data)):
#     if data_from[i][0:4] in user1:  #判断字符串是否在列表中
#         label.append(1)
#     elif data_to[i][0:4] in user1:
#         label.append(2)
#     else:
#         label.append(0)
#
# data2['label']=label
# for j in range(len(data2)):
#     if(data2['label'][j]==0 ):
#         data2.drop(j,inplace=True)
#
# data2.to_csv('data_merge/single/developer_email.csv',encoding='utf-8')  #得到developer的邮件记录
#
#
#




#==========================================developer邮件记录分析，收到的===========================================

# data=pd.read_csv('data_merge/single/developer_email.csv',encoding='utf-8')
#
# email_to=data['to']
# email_from=data['from']
#
# email_count1=[]   #to
# email_count2=[]   #from
#
#
# #2.1 匹配正则表达式,
# for j in range(len(email_to)):
#     if re.search(r'@hightech', email_from[j]):
#         # print(email_sip[i])
#         email_count2.append(0)
#     else:
#         email_count2.append(1)
# print(email_count2)
# #2.2 匹配正则表达式
# for j in range(len(email_from)):
#     if re.match(r'[0-9]{4}@hightech.com', email_to[j]):
#         # print(email_sip[i])
#         email_count1.append(1)
#
#     else:
#         email_count1.append(0)
# print(email_count1)
#
# #3.将只要有一个是0的行删除
# data['lable1'] = email_count1
# data['lable2'] = email_count2
# for j in range(len(data)):
#     if (data['lable1'][j]==0 or data['lable2'][j]==0):
#         #print(data[i-1]['from_new'][j])
#         data.drop(j,inplace=True)
# data.to_csv('data_merge/single/developer_email_receive_unusual.csv',encoding='utf-8')


#=======================================developer邮件记录分析，发送的==========================
# data=pd.read_csv('data_merge/single/developer_email.csv',encoding='utf-8')
#
# email_to=data['to']
# email_from=data['from']
#
# email_count1=[]  #from
# email_count2=[]  #to
#
#
# #2.1 匹配正则表达式,
# for j in range(len(email_to)):
#     if re.search(r'@hightech.com', email_to[j]):
#         # print(email_sip[i])
#         email_count2.append(0)
#     else:
#         email_count2.append(1)
# print(email_count2)
# #2.2 匹配正则表达式
# for j in range(len(email_from)):
#     if re.match(r'[0-9]{4}@hightech.com', email_from[j]):
#         # print(email_sip[i])
#         email_count1.append(1)
#
#     else:
#         email_count1.append(0)
# print(email_count1)
#
#
# #3.将只要有一个是0的行删除
# data['lable1'] = email_count1
# data['lable2'] = email_count2
# for j in range(len(data)):
#     if (data['lable1'][j]==0 or data['lable2'][j]==0):
#         #print(data[i-1]['from_new'][j])
#         data.drop(j,inplace=True)
# data.to_csv('data_merge/behavior/developer_email_send_unusual.csv',encoding='utf-8')


#=======================================developer垃圾邮件分析==========================

data=pd.read_csv('data_merge/behavior/developer_email_send_unusual.csv', encoding='utf-8')
dp_user=data.groupby('sip')
size=dp_user.size()
print(size)
