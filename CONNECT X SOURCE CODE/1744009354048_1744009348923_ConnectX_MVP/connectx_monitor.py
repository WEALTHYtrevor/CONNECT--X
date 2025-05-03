import pandas as pd
from ping3 import ping
from datetime import datetime
import json
from email_alert import send_alert

# Load config (IP addresses and ISPs)
with open('config.json') as f:
    config = json.load(f)

log = []

for ap in config['access_points']:
    ip = ap['ip']
    isp = ap['isp']
    response = ping(ip, timeout=2)

    status = 'Online' if response else 'Offline'
    response_time = round(response * 1000, 2) if response else None
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log.append({
        'Timestamp': timestamp,
        'IP Address': ip,
        'ISP': isp,
        'Status': status,
        'Response Time (ms)': response_time
    })

    if status == 'Offline':
        send_alert(ip, isp, timestamp)

# Save logs to CSV
df = pd.DataFrame(log)
df.to_csv('isp_data.csv', mode='a', header=not os.path.exists('isp_data.csv'), index=False)
print(df)