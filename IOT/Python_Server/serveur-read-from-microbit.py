# -*- coding: utf-8 -*-

import socket
import time
import datetime
import json
import serial
import threading
from clint.textui import colored

serial_port = 'COM6'
ser = serial.Serial(serial_port, 115200, timeout=1)

# Main
if __name__ == "__main__":
    while True:
        data = bytes.decode(ser.read(10000))
        if len(data)>0 :
            print(colored.red(f'\nData received from serial : {data}\n'))