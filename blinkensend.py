import socket
from array import array
import math
import time
import serial

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
    timeout=1,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

def gamma (x):
	if x==0:
		return 0
#	return 1.055*x**(2.4)-0.055
	return x**2.4

def sendFrame(time):
	data = array('B')
	for i in range(ledCount):
		for c in range(3):
			shifted_i = int(i + math.sin(time*0.3+(c/3))*10)
			brightness = 1.0/(ledCount+1)*(shifted_i+1)*2
#		brightness = int(brightness)
			if brightness>1 :
				brightness = 2.0 - brightness
			if brightness<0:
				brightness = 0
	#print(brightness)
	#print(int(gamma(brightness))*255, "!")
			brightness_byte = int(gamma(brightness)*255)
			data.append(brightness_byte)
	data.append("\n")
	ser.write(data)

startTime = time.time()
while True:
	t = time.time() - startTime
	sendFrame(t)
	time.sleep(0.036)


input("Press Enter to continue...")
