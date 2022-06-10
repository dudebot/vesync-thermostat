from functions import *
import asyncio

async def main():
	#turn on ac if weather >setpoint

	#load config
	config = load_config()
	weather = await getweather(config['location'])
	current_temp = weather['current_temp']
	print(f"current temp is :{current_temp}")
	if current_temp > config['setpoint']:
		print("setting device on")
		set_device_state(True)
	else:
		print("setting device off")
		set_device_state(False)

if __name__ == "__main__":
	asyncio.run(main())
