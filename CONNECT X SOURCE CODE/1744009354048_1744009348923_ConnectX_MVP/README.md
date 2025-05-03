# ConnectX MVP

## Description
This is a minimal viable product for ConnectX, a system that monitors access point connectivity and sends alerts to ISPs when internet connectivity fails.

## Setup
1. Install required Python packages:
   ```bash
   pip install pandas matplotlib ping3
   ```

2. Update email credentials in `email_alert.py`.

3. Run the monitor:
   ```bash
   python connectx_monitor.py
   ```

4. Visualize the logs:
   ```bash
   python graphs.py
   ```