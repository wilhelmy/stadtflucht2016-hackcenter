from array import array
import numpy as np
import math
import time
#import serial
import pyaudio as pa
from gui import GUI
import matplotlib.pyplot as plt

CHUNK = 1024
FORMAT = pa.paFloat32
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10
ledCount = 20

if __name__ == '__main__':

    p = pa.PyAudio()
    gui = GUI(ledCount)
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    #plt.ion();

    i=0
    oldsum=0
    #for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    def callback():
        global i, oldsum
        i += 1
        data = stream.read(CHUNK)
        #if i % 10 != 0: continue
        data = np.fromstring(data, 'Float32')
        fft_data = np.fft.fft(data)

        #l = len(fft_data)/2
        #a, b = l-20, l+20
        sum = 0
        for i in range(len(fft_data)):
            sum += fft_data[i]
            sum -= oldsum
            sum /= 15
            oldsum = sum

        nleds = min(ledCount, math.floor(math.sqrt(sum.real*sum.real + sum.imag*sum.imag)))
        for i in range(ledCount):
            if i < nleds:
                gui.color(i, "#ffffff")
            else:
                gui.color(i, "#000000")

        gui.after(16, callback)

        return

        freq = np.fft.fftfreq(fft_data.shape[-1])
        plt.plot(freq, fft_data.real, freq, fft_data.imag)
        plt.ylim(-100,100)
        plt.pause(0.005)
        plt.clf()
        #frames.append(data)
        #print(fft_data)

    callback()
    gui.mainloop()
    stream.stop_stream()
    stream.close()
    p.terminate()
