from array import array
import math
import time
#import serial

from gui import GUI

#ser = serial.Serial(
#    port='/dev/ttyACM0',
#    baudrate=9600,
#    timeout=1,
#    parity=serial.PARITY_NONE,
#    stopbits=serial.STOPBITS_ONE,
#    bytesize=serial.EIGHTBITS
#)

ledCount = 10

def gamma (x):
	if x==0:
		return 0
#	return 1.055*x**(2.4)-0.055
	return x**2.4

def pixel(time, i):
        color = [None, None, None] # R, G, B
	for c in range(3):
                shifted_i = int(i + math.sin(time*0.3+(c/3))*10)
                brightness = 1.0/(ledCount+1)*(shifted_i+1)*2
                if brightness>1 :
                        brightness = 2.0 - brightness
                if brightness<0:
                        brightness = 0
		brightness_byte = int(gamma(brightness)*255)
                color[c] = brightness_byte
        return color

def sendFrame(time):
        """send frame over the serial console"""
	data = array('B')
	for i in range(ledCount):
                pix = pixel(time, i)
                data.append(*pix)
	data.append(ord("\n"))
	ser.write(data)

def guiFrame(gui, time):
        """display frame on the GUI"""
        for i in range(ledCount):
                color = "#%02x%02x%02x" % tuple(pixel(time, i))
                gui.color(i, color)

if __name__ == '__main__':
        gui = GUI(ledCount)
        startTime = time.time()
        def callback():
                t = time.time() - startTime
                guiFrame(gui, t)
                gui.after(16, callback) # ~60fps
        callback()
        gui.mainloop()
