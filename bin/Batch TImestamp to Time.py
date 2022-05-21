import datetime
import pandas as pd

df = pd.read_csv('dataset.csv') #读取

# 将时间戳转化为时间
df['date_time'] = df['ctime'].apply(lambda x: datetime.datetime.fromtimestamp(x))
df.to_csv('output.csv', index=False) #导出到csv