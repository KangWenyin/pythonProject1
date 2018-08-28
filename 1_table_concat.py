import pandas as pd
import re
import os
#====================将文件夹批量化处理成字典=============================================

a=os.listdir('data') #['2017-11-01', '2017-11-02', '2017-11-03', '2017-11-04'..]
info1=[]  #存放路径 data/2017-11-01
info2=['/checking.csv', '/email.csv', '/login.csv', '/tcpLog.csv', '/weblog.csv']  #存放路径 data/2017-11-01后面的checking.csv等
for i in range(len(a)):
    info1.append(os.path.join('data',a[i]))       #将路径与文件名结合起来就是每个文件的完整路径
data_path={}
for i in range(1,31):
    for j in range(len(info2)):
        data_path.setdefault(i,[])
        data_path[i].append(info1[i-1]+info2[j])
print(data_path)  #{1: [4个文件], 2: [4个文件]，..]
#======================================读数据===============================

#
# #1.批量读入email.csv的数据
# data1=[0]*30  #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(1,31):
#     data1[i-1]=pd.read_csv(data_path[i][1],encoding='utf-8')
#     print(i-1)
#     #print(type(data1))  #<class 'list'>
# #print(type(data1[0]))  #<class 'pandas.core.frame.DataFrame'>
# a=pd.concat(data1)
# a.to_csv('data_merge/all/all_email.csv',encoding='utf-8')  #写入文件
#
# #2.批量读入checking.csv的数据
# data2=[0]*30
# for i in range(1,31):
#     data2[i-1]=pd.read_csv(data_path[i][0],encoding='utf-8')
#
# a=pd.concat(data2)
# a.to_csv('data_merge/all/all_checking.csv',encoding='utf-8')
#
# #3.批量读入login.csv的数据
# data3=[0]*30
# print(data3)
# for i in range(1,31):
#     data3[i-1]=pd.read_csv(data_path[i][2])
#
# a=pd.concat(data3)
# a.to_csv('data_merge/all/all_login.csv')

#4.批量读入tcpLog.csv的数据
# data4_1=[0]*5
# print(data4_1)
# for i in range(1,6):
#     data4_1[i-1]=pd.read_csv(data_path[i][3],encoding='utf-8')
#     print(i)
#
# a=pd.concat(data4_1)
# a.to_csv('data_merge/all/all_tcpLog_week1.csv',encoding='utf-8')
#
# data4_2=[0]*7
# print(data4_2)
# for i in range(6,13):
#     data4_2[i-6]=pd.read_csv(data_path[i][3],encoding='utf-8')
#     print(i)
#
# b=pd.concat(data4_2)
# b.to_csv('data_merge/all/all_tcpLog_week2.csv',encoding='utf-8')
#
# data4_3=[0]*7
# print(data4_3)
# for i in range(13,20):
#     data4_3[i-13]=pd.read_csv(data_path[i][3],encoding='utf-8')
#     print(i)
#
# b=pd.concat(data4_3)
# b.to_csv('data_merge/all/all_tcpLog_week3.csv',encoding='utf-8')
#
#
# data4_4=[0]*7
# print(data4_4)
# for i in range(20,27):
#     data4_4[i-20]=pd.read_csv(data_path[i][3],encoding='utf-8')
#     print(i)
#
# a=pd.concat(data4_4)
# a.to_csv('data_merge/all/all_tcpLog_week4.csv',encoding='utf-8')
#
# data4_5=[0]*4
# print(data4_5)
# for i in range(27,31):
#     data4_5[i-27]=pd.read_csv(data_path[i][3],encoding='utf-8')
#     print(i)
#
# a=pd.concat(data4_5)
# a.to_csv('data_merge/all/all_tcpLog_week5.csv',encoding='utf-8')
#
# #5.批量读入weblog.csv的数据
# data5=[0]*30
# print(data5)
# for i in range(1,31):
#     data5[i-1]=pd.read_csv(data_path[i][4],encoding='utf-8')
#     print(i)
#
# a=pd.concat(data5)
# a.to_csv('data_merge/all/all_weblog.csv',encoding='utf-8')
