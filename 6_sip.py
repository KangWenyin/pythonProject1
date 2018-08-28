import pandas as pd
import re
data=pd.read_csv('data/2017-11-01/email.csv',encoding='utf-8')
email_sip=data['sip']
email_from=data['from']

sip1=[]
for j in range(len(email_sip)):
    if re.match(r'10.64.106', email_sip[j]):
        # print(email_sip[i])
        sip1.append(int(email_sip[j][10:]))
    else:
        sip1.append(0)
print(sip1) #{1:[0,0,235,0,0,7,0],2:[],..30:[]}

sip2=[]
for j in range(len(email_sip)):
    if re.match(r'10.64.105', email_sip[j]):
        # print(email_sip[i])
        sip2.append(int(email_sip[j][10:]))
    else:
        sip2.append(0)
print(sip2) #{1:[0,0,235,0,0,7,0],2:[],..30:[]}

a=sorted(list(set(sip1)))
b=sorted(list(set(sip2)))
print(a)
print(len(a))
print('')
print(b)
print(len(b))