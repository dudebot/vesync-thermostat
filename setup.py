from pyvesync import VeSync
import base64
import json

username = input("email: ")

password = input("password: ")

#setup config
manager = VeSync(username, password)
manager.login()
manager.update()

for index, outlet in enumerate(manager.outlets):
    print(index, outlet.device_name)

device_num = int(input("Select device #"))

device = manager.outlets[device_num]
device_name = manager.outlets[device_num].device_name

print("Writing config.txt")

config_json = {"username":username,
               "password":base64.b64encode(password.encode('ascii')).decode('ascii'),
               "device":device_name}

json.dump(config_json,fp=open("config.txt",'w'))
