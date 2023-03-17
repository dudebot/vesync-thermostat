from pyvesync import VeSync
from functions import *


async def main():
    username = input("Enter vesync email: ")
    password = input("Enter vesync password: ")

    manager = VeSync(username, password)
    manager.login()
    manager.update()

    for index, outlet in enumerate(manager.outlets):
        print(index, outlet.device_name)

    print("Logging in to list devices...")
    device_num = int(input("Select device # "))

    device_name = manager.outlets[device_num].device_name

    valid_temp = False
    while not valid_temp:
        temp = input("Enter setpoint temp: ")
        try:
            temp = int(temp)
            valid_temp = True
        except:
            print("Invalid temp")

    valid_location = False
    while not valid_location:
        location = input("Enter location (example Dallas, TX): ")
        weather_data = await getweather(location)
        correct = input(f"Current temp is {weather_data['current_temp']}, does this look correct? (y/n): ")
        if correct.lower() in ['y', 'yes']:
            valid_location = True

    print("Writing config.json")

    config_json = {"username": username,
                   "password": base64.b64encode(password.encode('ascii')).decode('ascii'),
                   "device": device_name,
                   "setpoint": temp,
                   "location": location}

    json.dump(config_json, fp=open("config.json", 'w'))

if __name__ == "__main__":
	asyncio.run(main())
