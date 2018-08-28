# -*- coding: utf-8 -*-

import pandas as pd
import time
import matplotlib.pyplot as plt


def countTimeNum(time_str, checkin):
    # 分别记录没签到人数，8:00-8:10之间的人数，10分为一个间隔依次类推
    # time_str = ['没签到人数','08:00','08:10','08:20','08:30','08:40','08:50','09:00','9点之后']
    # checkin = data_hr['checkin'].tolist()
    time_num = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    time_stamp = [0]
    for i in range(1, len(time_str) - 1):
        t = '2017-11-01 ' + time_str[i]
        print(1,t)
        # 转换成时间数组
        timeArray = time.strptime(t, "%Y-%m-%d %H:%M")
        print(3,timeArray)
        # 转换成时间戳
        timestamp = time.mktime(timeArray)
        print(4,timestamp)
        time_stamp.append(timestamp)

    for i in range(len(checkin)):
        if checkin[i] == '0':
            time_num[0] = time_num[0] + 1
        else:
            d = checkin[i].split()
            print(5,d)
            timeStr = d[1]
            print(6,timeStr)
            num = timeStr.count(':')
            if num == 2:
                index = timeStr.find(':', 3)
                t1 = timeStr[0:index]
                timeStr = '2017-11-01 ' + t1
            else:
                timeStr = '2017-11-01 ' + timeStr
            print(2,timeStr)
            # 转换成时间数组
            timeArray = time.strptime(timeStr, "%Y-%m-%d %H:%M")
            # 转换成时间戳
            timestamp = time.mktime(timeArray)

            time_index = 0
            for j in range(1, len(time_stamp)):
                if timestamp > time_stamp[j - 1] and timestamp < time_stamp[j]:
                    time_index = j
                    break

            if time_index == 0:
                time_num[-1] = time_num[-1] + 1
            else:
                time_num[time_index] = time_num[time_index] + 1

    return time_num


# 读取签到CSV表格数据
data = pd.read_csv('data_merge/all/all_checking.csv', encoding='utf-8')
# hr用户ID号
hr_list = [1013, 1104, 1110, 1118, 1149, 1165, 1184, 1249, 1251, 1295, 1300, 1312, 1363, 1371, 1378, 1433, 1473, 1499]

# 获取所有HR每天的签到记录
label = []
data_id = data['id'].tolist()
for j in range(len(data_id)):
    if data_id[j] in hr_list:
        label.append(1)
    else:
        label.append(0)

data['label'] = label
data_hr = data.loc[data['label'] == 1]
data_hr = data_hr.drop(['label'], axis=1)

# 上班记录没签到人数，8:00之前的人数，8:00-8:10之间的人数，10分为一个间隔依次类推
time_strIn = ['not checkIn', '08:00', '08:10', '08:20', '08:30', '08:40', '08:50', '09:00', 'after 09:00']
checkin = data_hr['checkin'].tolist()
checkinNum = countTimeNum(time_strIn, checkin)

# 下班记录没签到人数，18:00之前的人数，18:00-18:30之间的人数，30分为一个间隔依次类推
time_strOut = ['not checkOut', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', 'after 21:00']
checkout = data_hr['checkout'].tolist()
checkoutNum = countTimeNum(time_strOut, checkout)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

plt.subplot(2, 1, 1)
plt.plot(x, checkinNum, 'o-')
plt.bar(x, checkinNum)
plt.xticks(x, time_strIn, rotation=0)
plt.title('checkIn & checkout')
plt.xlabel('time (10s)')
plt.ylabel('Number')

plt.subplot(2, 1, 2)
plt.plot(x, checkoutNum, '.-')
plt.bar(x, checkoutNum)
plt.xticks(x, time_strOut, rotation=0)
plt.xlabel('time (30s)')
plt.ylabel('Number')

plt.show()





