from array import array
import numpy as np
import math
import time
#import serial
import pyaudio as pa

import gui

CHUNK = 1024
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10

if __name__ == '__main__':
    p = pa.PyAudio()
    gui = GUI()
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = numpy.fromstring(stream.read(CHUNK), 'Int16')
        frames.append(data)
        print(data)

    stream.stop_stream()
    stream.close()
    p.terminate()
