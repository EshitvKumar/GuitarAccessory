from soundhandler import *
import keyboard

try:
  with sd.InputStream(channels = 1,
                      callback = callback,
                      blocksize = WINDOW_STEP,
                      samplerate = SAMPLE_FREQ):
    while True:
        if keyboard.is_pressed('q'):
          break
    
except Exception as e:
    print(str(e))