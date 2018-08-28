import pandas as pd
import re
import os
import numpy as np

#1.
# data=pd.read_csv('data_merge/behavior/tcp1.csv',encoding='utf-8') #计算财务部的数据
#2.
data=pd.read_csv('data_merge/single/web_tcp_user_1.csv',encoding='utf-8')  #计算所有人的数据
data1=data.groupby('host')
print(data1)
user_num=data1.size()
print(user_num)
print(len(user_num))
print(type(user_num))
user_num.to_csv('data_merge/behavior/web_tcp_user_1_num.csv',encoding='utf-8')

# #====================================计算hr的tcp的发送和接收数据=======================
# uplink_length_1=data['uplink_length']
# downlink_length=data['downlink_length']
# # a=data.describe()
# # print(a)
#
# print(type(uplink_length_1))
# a=uplink_length_1.describe()
# print(a)
# uplink_length=uplink_length_1.values
# b=pd.cut(uplink_length,20)
# c=b.codes
# d=pd.value_counts(b)
# print(c)
# print(d)
#
# bb=b[:2]
# print(1,b)
# print(2,bb)
#
# def get_stats(group):
#     return{'min':group.min(),'max':group.max(),'count':group.count(),'mean':group.mean()}
#
# group=uplink_length_1.groupby(b)
# g1=group.apply(get_stats).unstack()
# print(g1)

# #====================================计算hr的email的发送和接收数据=======================























