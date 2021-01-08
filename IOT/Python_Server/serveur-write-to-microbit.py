# -*- coding: utf-8 -*-

import socket
import time
import datetime
import json
import serial
import threading
import urllib.request
from clint.textui import colored

serial_port = 'COM6'
ser = serial.Serial(serial_port, 115200, timeout=1)


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



# Main
if __name__ == "__main__":
    while True:
       try:
        link = "http://localhost/feu/Simulator/FEU/liste.php"
        f = urllib.request.urlopen(link)
        json_data= f.read()
        parsedJson = json.loads(json_data)
        for i in range(0,len(parsedJson["feux"])):
                print(parsedJson["feux"][i])
                my_dict = parsedJson["feux"][i]
                latitude = '{'+ encrypt('"la":' + str(my_dict["lat"]),3) + '}'
                longitude = '{'+ encrypt('"lo":' + str(my_dict["lon"]),3) + '}'
                intensite = '{'+ encrypt('"in":' + str(my_dict["intensite"]),3) + '}'
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
       except:
           pass