from array import array
import numpy as np
import math
import time
import serial
import pyaudio as pa

p = pa.PyAudio()
CHUNK = 1024
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

while True:
    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = []
        data = stream.read(CHUNK)
        frames.append(data)
        print(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()
