def on_received_string(receivedString):
    global sizeofpacket, sender_adress
    sizeofpacket = len(receivedString)
    sender_adress = receivedString.substr(0, 3)
    basic.pause(100)
    if sender_adress == friend_id:
        serial.write_string("" + receivedString.substr(3, sizeofpacket) + "}")
radio.on_received_string(on_received_string)

sender_adress = ""
sizeofpacket = 0
friend_id = ""
SerialRead = ""
my_id = "GT"
friend_id = "REC"
basic.show_string("Gtw")
radio.set_group(1)
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE115200)

def on_forever():
    pass
basic.forever(on_forever)
