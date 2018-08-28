import pandas as pd

# data_web=pd.read_csv('data_merge/all/all_weblog.csv',encoding='utf-8')
# data_tcp_1=pd.read_csv('data_merge/all/all_tcpLog_week1.csv',encoding='utf-8')

#pd.merge(data_web,data_tcp_1,left_on=[])


login_user=pd.read_csv('data_merge/single/login_user.csv',encoding='utf-8')
login_user_list=login_user.values
login_list=login_user_list.tolist()
print(login_list)

#处理嵌套列表
def flat(all):
    for k in all:
        if not isinstance(k, (list, tuple)):
            yield k
        else:
            yield from flat(k)
b=list(flat(login_list))
print(b)  #得到login的id
print(len(b))

hr_id=[1013, 1104, 1110, 1118, 1149, 1165, 1184, 1249, 1251, 1295, 1300, 1312, 1363, 1371, 1378, 1433, 1473, 1499]
financial_id=[1293, 1041, 1431, 1180, 1439, 1186, 1451, 1327, 1467, 1213, 1342, 1346, 1347, 1226, 1108, 1368, 1369, 1370, 1498, 1248, 1124, 1253, 1255, 1137]
a=list(set(hr_id).intersection(set(b)))
print(a)
aa=list(set(financial_id).intersection(set(b)))
print(aa)
aa1=list(set(financial_id).intersection(set(hr_id)))
print(aa1)

a=list(set(hr_id).union(set(b)))
print(a)
aa=list(set(a).union(set(financial_id)))
print(aa)
print(len(aa))

checking_id=pd.read_csv('data_merge/single/checking_id.csv',encoding='utf-8')
ck_id=checking_id['id']
ck=ck_id.values
ck_list=ck.tolist()
print(len(ck_list))
ass=list(set(ck_list).difference(set(aa)))
print(ass)
#
# aa=list(set(financial_id).intersection(set(b)))
# print(aa)
# aa1=list(set(financial_id).intersection(set(hr_id)))
# print(aa1)

#
# aaa=b.append(hr_id)
# aaa=[i for i ]
# print(aaa)
# # aaaa=aaa.append(financial_id)
# # print(aaaa)
