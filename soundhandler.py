import sounddevice as sd
import numpy as np
import scipy.fftpack
import os
from funcs import *

# General settings
SAMPLE_FREQ = 44100
WINDOW_SIZE = 44100
WINDOW_STEP = 21050
WINDOW_T_LEN = WINDOW_SIZE / SAMPLE_FREQ
SAMPLE_T_LENGTH = 1 / SAMPLE_FREQ
windowSamples = [0 for _ in range(WINDOW_SIZE)]

# The sounddecive callback function
def callback(indata, frames, time, status):
  global windowSamples
  if status:
    print(status)
  if any(indata):
    windowSamples = np.concatenate((windowSamples,indata[:, 0])) # append new samples
    windowSamples = windowSamples[len(indata[:, 0]):] # remove old samples
    magnitudeSpec = abs(scipy.fftpack.fft(windowSamples)[:len(windowSamples)//2] )

    for i in range(int(62/(SAMPLE_FREQ/WINDOW_SIZE))):
      magnitudeSpec[i] = 0 #suppress mains hum

    maxInd = np.argmax(magnitudeSpec)
    maxFreq = int(maxInd * (SAMPLE_FREQ/WINDOW_SIZE))
    closestPitch, closestNote  = getClosestGuitarNote(maxFreq)
    closestPitch = int(closestPitch)

    os.system('cls' if os.name=='nt' else 'clear')
    if closestPitch < maxFreq:
      print(f"{closestNote}: {closestPitch} v {maxFreq}")
    else:
      print(f"{closestNote}: {closestPitch} ^ {maxFreq}")
  else:
    print('no input')
