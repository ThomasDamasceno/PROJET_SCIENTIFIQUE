# -*- coding: utf-8 -*-

import socket
import time
import datetime
import json
import serial
import threading
from clint.textui import colored

serial_port = 'COM5'
ser = serial.Serial(serial_port, 115200, timeout=1)

json_data= '{"position":{"latitude":45.516,"longitude":-122.636},"intensite":75}'

my_dict = json.loads(json_data)
latitude = '{"la" : "' + str(my_dict["position"]["latitude"]) + '"}'
longitude = '{"lo" : "' + str(my_dict["position"]["longitude"]) + '"}'
intensite = '{"in" : "' + str(my_dict["intensite"]) + '"}'

# Main
if __name__ == "__main__":
    while True:
        time.sleep(2)
        ser.write(latitude.encode())
        print(colored.blue(f'\nlatitude sent to serial : {latitude}\n'))
        time.sleep(2)
        ser.write(longitude.encode())
        print(colored.blue(f'\nlongitude sent to serial : {longitude}\n'))
        time.sleep(2)
        ser.write(intensite.encode())
        print(colored.blue(f'\nintensite du feu sent to serial : {intensite}\n'))
