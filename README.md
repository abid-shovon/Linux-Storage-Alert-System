
# Disk Usage Monitor with Email Alert (Linux Only)

> **This script works only in Linux OS environments**, since it uses the `df -h` command to read disk usage data.

## Description

This Python script monitors disk usage on a Linux machine.  
When any partition's usage **reaches or exceeds a defined threshold** (e.g., 90%), it sends an **email alert** to a specified email address.

This is helpful for:
- Server monitoring
- Personal laptop/desktop health checks
- Avoiding storage crashes or space issues

---


## Requirements

- Python 3
- Linux OS (Ubuntu, Debian, Fedora etc.)
- Internet access
- A Gmail account with **App Passwords enabled**
