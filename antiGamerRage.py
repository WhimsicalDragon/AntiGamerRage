import sounddevice as sd
import numpy as np

global stopStream
stopStream = 0

def print_sound(indata, outdata, frames, time, status):
    global stopStream
    volume_norm = np.linalg.norm(indata)*10
    #print ("|" * int(volume_norm))
    print(volume_norm)

    if volume_norm > 40 :
        print("Loud gamer!")
        stopStream = 1


#while stopStream == 0:
with sd.Stream(callback=print_sound):
    pass
    while stopStream == 0:
        pass
    sd.sleep(100)

print("Done!")

