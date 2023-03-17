Quick stateless script to turn on or off a vesync device if the weather is above a setpoint temperature
# Setup
- Run setup.py to generate login config. It will prompt for email, password, then request which device to handle. Enter the number of the device.
```
Enter vesync email: [your vesync email]
Enter vesync password: [redacted]
0 Radiator
1 Air Conditioning
2 Screen
3 Sanitize
4 Christmas lights
5 Fan
6 Desk Light
7 Reading
8 Downstairs fan
Logging in to list devices...
Select device # 1
Enter setpoint temp: 83
Enter location (example Dallas, TX): dallas tx
Current temp is 100, does this look correct? (y/n): yes
Writing config.json
```

# Usage
```
python3 thermostat.py
```

# Example crontab
*/10 * * * * cd /home/pi/vesync-thermostat/ && /usr/bin/python3 /home/pi/vesync-thermostat/thermostat.py
