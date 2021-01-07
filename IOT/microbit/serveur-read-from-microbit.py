import socket
import time
import datetime
import json
import serial
import threading
from clint.textui import colored
import paho.mqtt.client as paho

serial_port = 'COM5'
ser = serial.Serial(serial_port, 115200, timeout=1)
broker = "vpn.goneix.net"
port = 1883
def on_publish(client,userdata,result): #create function for callback
    print("data published \n")
    pass
client1= paho.Client("control1") #create client object
client1.on_publish = on_publish #assign function to callback
client1.connect(broker,port) #establish connection
data_concat =''
flag = False
def chr_to_ascii(char = 'A'): 
    liste = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
    return liste.index(char)

def ascii_to_chr(code_ascii = 0):
    liste = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
    return liste[code_ascii]

def encrypt(string_to_encrypte = 'a', key = 0):
    encrypted_string = ''

def decrypt(string_to_encrypte = 'a', key = 0):
    encrypted_string = ''
    c = 0
    for ch in string_to_encrypte :
        c = chr_to_ascii(ch) - key
        c = c + 95
        c = c%95
        encrypted_string += ascii_to_chr(c)
    return encrypted_string

# Main
if __name__ == "__main__":
    while True:
        data = bytes.decode(ser.read(10000),"ascii")
        data = decrypt(data[1:-1],3)
        if len(data)>0 :
            print(colored.red(f'\nData received from serial : {data}\n'))
            if data == 'S':
                flag = True
            elif data =='s':
                flag = False
                data_concat = data_concat.replace("}{",",")
                # data_concat = data_concat.replace("}","")
                # data_concat = data_concat.replace("{","")
                if len(data_concat)>=20:
                    print(colored.yellow(data_concat))
                    try:
                        jsonn = json.loads(data_concat)
                        lat = jsonn["la"]
                        lo = jsonn["lo"]
                        inte = jsonn["in"]
                        client1.publish(f"alarm/{lat}:{lo}/fire",float(inte))
                    except:
                        pass
                data_concat = ''  
            if flag == True and data != 'S':
                    data = "{" + data + "}"
                    data_concat += data
            