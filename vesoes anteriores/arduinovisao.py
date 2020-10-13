import serial
import time
import os
from serial import Serial

def arduino():
    try:
        ser = Serial(
            port='/dev/ttyACM0',
            baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1)

        ser.write(str.encode('w')) 
        time.sleep(1) 
        ser.write(str.encode('s'))  
        print("Arduino ok")
    except:
        print("Erro arduino nao conectado") 
