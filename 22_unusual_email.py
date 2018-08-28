import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

#=============================error=====================================
data1=pd.read_csv('data_merge/behavior/developer_from_unusual.csv',encoding='utf-8')
data2=data1.groupby('to').size()
print(data2)
print('=================')
data3=data2.sort_values()
print(data3)
print(len(data3))
