def on_data_received():
    global SerialRead, packet
    SerialRead = serial.read_until("}")
    pause(200)
    packet = "" + my_id + SerialRead
    # basic.show_string(SerialRead)
    radio.send_string(packet)
serial.on_data_received("{", on_data_received)

packet = ""
SerialRead = ""
my_id = ""
basic.show_string("Rec")
radio.set_group(1)
my_id = "REC"
friend_id = "GT"
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE115200)

def on_forever():
    serial.read_string()
basic.forever(on_forever)
