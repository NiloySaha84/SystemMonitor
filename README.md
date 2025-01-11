# System Health Monitor

This Python script monitors the health of your system by tracking CPU usage, disk space, and network usage. If any of these parameters exceed a set threshold, the script will send an email alert. It also logs the system data in a JSON file for future reference.

## Features

- **CPU Usage Monitoring**: Checks CPU usage and sends an alert if it exceeds 80%.
- **Disk Usage Monitoring**: Monitors disk space usage and alerts if it exceeds 90%.
- **Network Monitoring**: Tracks the number of bytes sent over the network and sends an alert if it exceeds 1GB.
- **JSON Logging**: Logs system data (timestamp, CPU, disk, network usage) in a JSON file.
- **Email Alerts**: Sends alerts via email (using Gmail SMTP server) when any threshold is crossed.

## Prerequisites

To run this script, the following Python libraries are required:

- **psutil**: For monitoring system usage.
- **smtplib**: For sending email alerts.
- **email.mime**: For constructing email messages.
- **json**: For saving system data in a JSON file.

## File Format

The system health data is saved in a JSON file (systemMonitor.json). Each entry contains:

-	**timestamp**: The timestamp of when the monitoring data was collected.
-	**cpu_usage**: The percentage of CPU usage at the time of monitoring.
-	**disk_percent**: The percentage of disk space used at the time of monitoring.
-	**net**: The number of bytes sent over the network.

 ## Scheduling the Script
 
 The script is scheduled to run automatically using **Cron**.

 ## License

 This project is licensed under the **MIT License**.

 
