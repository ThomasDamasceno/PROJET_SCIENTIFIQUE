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

json_data= '{"position":{"latitude":45.516,"longitude":-122.636},"intensite":75}'

def chr_to_ascii(char = 'A'): 
    liste = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
    return liste.index(char)

def ascii_to_chr(code_ascii = 0):
    liste = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
    return liste[code_ascii]

def encrypt(string_to_encrypte = 'a', key = 0):
    encrypted_string = ''
    c = 0
    for ch in string_to_encrypte :
        c = (chr_to_ascii(ch) + key)%95
        encrypted_string += ascii_to_chr(c)
    return encrypted_string


my_dict = json.loads(json_data)
latitude = '{'+ encrypt('"la" : ' + str(my_dict["position"]["latitude"]),3) + '}'
longitude = '{'+ encrypt('"lo" : ' + str(my_dict["position"]["longitude"]),3) + '}'
intensite = '{'+ encrypt('"in" : ' + str(my_dict["intensite"]),3) + '}'


# Main
if __name__ == "__main__":
    while True:
        ser.write(str('{'+encrypt("S",3)+'}').encode())
        time.sleep(2)
        ser.write(latitude.encode("ascii"))
        print(colored.blue(f'\nlatitude sent to serial : {latitude}\n'))
        time.sleep(2)
        ser.write(longitude.encode("ascii"))
        print(colored.blue(f'\nlongitude sent to serial : {longitude}\n'))
        time.sleep(2)
        ser.write(intensite.encode("ascii"))
        print(colored.blue(f'\nintensite du feu sent to serial : {intensite}\n'))
        time.sleep(2)
        ser.write(str('{'+encrypt("s",3)+'}').encode("ascii"))
        time.sleep(2)