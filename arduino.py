import serial
import time

ser = serial.Serial('COM3', 9600)

print(ser.write(b'H'))

