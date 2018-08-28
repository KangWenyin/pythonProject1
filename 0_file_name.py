import os
#====================将文件夹批量化处理成字典{1: [4个文件名字], 2: [4个文件名字]，..]=============================================

a=os.listdir('data') #['2017-11-01', '2017-11-02', '2017-11-03', '2017-11-04'..]
info1=[]  #存放路径 data/2017-11-01
info2=['/checking.csv', '/email.csv', '/login.csv', '/weblog.csv','/tcpLog.csv']  #存放路径 data/2017-11-01后面的checking.csv等
for i in range(len(a)):
    info1.append(os.path.join('data',a[i]))       #将路径与文件名结合起来就是每个文件的完整路径
data_path={}
for i in range(1,31):
    for j in range(len(info2)):
        data_path.setdefault(i,[])
        data_path[i].append(info1[i-1]+info2[j])
print(data_path)  #{1: [4个文件], 2: [4个文件]，..]

