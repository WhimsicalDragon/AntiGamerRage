import sounddevice as sd
import numpy as np
import os
import subprocess

global stopStream
stopStream = 0
os.chdir("Cornhacks")
def print_sound(indata, outdata, frames, time, status):
    global stopStream
    volume_norm = np.linalg.norm(indata)*10
    print(volume_norm)

    if volume_norm > 40 :
        print("Loud gamer!")
        stopStream = 1
        os.system("cd")
        os.system("cscript.exe GUI.vbs")

        f = open("answer.txt", "r")
        if f.read(5) == "No\n" :
            os.system("start firefox.exe https://www.youtube.com/watch?v=V1RPi2MYptM")

with sd.Stream(callback=print_sound):
    pass
    while True :
        pass
    sd.sleep(100)

print("Done!")

