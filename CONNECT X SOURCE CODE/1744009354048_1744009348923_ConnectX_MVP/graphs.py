import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('isp_data.csv')

# Connectivity status count
status_count = df['Status'].value_counts()
status_count.plot(kind='bar', color=['green', 'red'], title='Connectivity Status')
plt.show()

# ISP Performance
status_by_isp = df.groupby(['ISP', 'Status']).size().unstack()
status_by_isp.plot(kind='bar', stacked=True, title='ISP-wise Status')
plt.show()

# Response time trends
df_online = df[df['Status'] == 'Online']
df_online['Timestamp'] = pd.to_datetime(df_online['Timestamp'])
df_online.plot(x='Timestamp', y='Response Time (ms)', title='Response Time Trend')
plt.xticks(rotation=45)
plt.show()