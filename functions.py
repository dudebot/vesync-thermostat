from pyvesync import VeSync
import base64
import json

import python_weather
import asyncio

def set_device_state(turn_on):
    #load config
    config = json.load(open('config.json'))
    manager = VeSync(config['username'], base64.b64decode(config['password']).decode('ascii'))
    manager.login()
    manager.update()

    found = False
    for outlet in manager.outlets:
        if outlet.device_name==config['device']:
            if turn_on:
                outlet.turn_on()
            else:
                outlet.turn_off()
            return found

    if not found:
        print(f"Device {config['device']} not found. Please delete config.json and re-run")

def toggle_device_state():
    #load config
    config = json.load(open('config.json'))
    manager = VeSync(config['username'], base64.b64decode(config['password']).decode('ascii'))
    manager.login()
    manager.update()

    found = False
    for outlet in manager.outlets:
        if outlet.device_name==config['device']:
            if outlet.is_on:
                outlet.turn_off()
            else:
                outlet.turn_on()

            return outlet

    if not found:
        print(f"Device {config['device']} not found. Please delete config.json and re-run")
        
def get_device():
    #load config
    config = json.load(open('config.json'))
    manager = VeSync(config['username'], base64.b64decode(config['password']).decode('ascii'))
    manager.login()
    manager.update()
    print(config)
    found = False
    for outlet in manager.outlets:
        if outlet.device_name==config['device']:
            return outlet

    if not found:
        print(f"Device {config['device']} not found. Please delete config.json and re-run")

def load_config():
    config = json.load(open('config.json'))
    config['password'] = base64.b64decode(config['password']).decode('ascii')
    return config

async def getweather(location):
    result = {}
    
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # fetch a weather forecast from a city
    weather = await client.find(location)

    # returns the current day's forecast temperature (int)
    result['current_temp'] = int(weather.current.temperature)
    result['forecast']=[[i.date,i.low,i.high] for i in weather.forecasts]
    
    # close the wrapper once done
    await client.close()
    
    return result
