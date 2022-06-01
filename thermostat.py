from functions import *
import asyncio

async def main():
	#turn on ac if weather >85
	weather = await getweather()
	current_temp = int(weather['current_temp'])
	print(f"current temp is :{current_temp}")
	if current_temp > 85:
		print("setting device on")
		set_device_state(True)
	else:
		print("setting device off")
		set_device_state(False)

if __name__ == "__main__":
	asyncio.run(main())
