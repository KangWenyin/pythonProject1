import pandas as pd

hr=[1013, 1104, 1110, 1118, 1149, 1165, 1184, 1249, 1251, 1295, 1300, 1312, 1363, 1371, 1378, 1433, 1473, 1499]
financial=[1293, 1041, 1431, 1180, 1439, 1186, 1451, 1327, 1467, 1213, 1342, 1346, 1347, 1226, 1108, 1368, 1369, 1370, 1498, 1248, 1124, 1253, 1255, 1137]

ck=pd.read_csv('data_merge/all/all_checking.csv',encoding='utf-8')
ck_id=ck['id'].unique()
#print(len(ck_id)) #299
ck_id=ck_id.tolist()

#0.测试hr和financial的交集，为空

# a=list(set(hr).intersection(set(financial)))
# print(a)

#1.得到hr和financial的并集h_f，为42

h_f=list(set(hr).union(set(financial)))
print(h_f)
print(len(h_f)) #42

#2.得到h_f和ck_id的差集r_d,即研发部门的人
r_d=list(set(ck_id).difference(set(h_f)))
print(r_d)
print(len(r_d))  #257