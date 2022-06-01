Quick stateless script to turn on a vesync device if the weather (hardcoded for dallas) is above 85F (also hardcoded lol).  

# Setup
- Run setup.py to generate login config. It will prompt for email, password, then request which device to handle. Enter the number of the device.
```
 python3 setup.py
email: [redacted]
password: [redacted]
0 Radiator
1 Air Conditioning
2 Screen
3 Christmas lights
...
Select device #1
```

# example crontab (assuming /home/pi/vesync-thermostat/ is the cloned directory: 
*/10 * * * * cd /home/pi/vesync-thermostat/ && /usr/bin/python3 /home/pi/vesync-thermostat/thermostat.py
