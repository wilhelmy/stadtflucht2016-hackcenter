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

if __name__ == '__main__':

    p = pa.PyAudio()
    #gui = GUI(10,)
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    plt.ion();

    i=0
    #for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    while True:
        i += 1
        data = stream.read(CHUNK)
        if i % 10 != 0: continue
        data = np.fromstring(data, 'Float32')
        fft_data = np.fft.fft(data)

        freq = np.fft.fftfreq(fft_data.shape[-1])
        plt.plot(freq, fft_data.real, freq, fft_data.imag)
        plt.ylim(-100,100)
        plt.pause(0.005)
        plt.clf()
        #frames.append(data)
        #print(fft_data)

    stream.stop_stream()
    stream.close()
    p.terminate()
