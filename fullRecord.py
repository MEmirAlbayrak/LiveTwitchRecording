from selenium import webdriver
import time
import datetime
import json
import re
import os
from skimage.metrics import structural_similarity as ssim

import cv2
import numpy as np
import pyautogui

from multiprocessing import Process


def video():
    driver = webdriver.Chrome()


    pattern = r'https:\/\/(.*)\.com\.tr'

    site = "https://www.twitch.tv/admiralbahroo"
    driver.maximize_window()
    driver.get(site)
    # driver.refresh()

    chrome_options = webdriver.ChromeOptions()

    print (site)
    print(type(site))
    time.sleep(3)
    pyautogui.press('f')
    time.sleep(1)

    SCREEN_SIZE = (1920, 1080)

    fourcc = cv2.VideoWriter_fourcc(*"XVID")

    out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

    while True:
        img = pyautogui.screenshot()

        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        out.write(frame)

        cv2.imshow("screenshot", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    # make sure everything is closed when exited
    cv2.destroyAllWindows()
    out.release()

    driver.close()



import pyaudio
import wave

def audio():

    

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "output.mp3"
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    time.sleep(4)
    print("* recording")
    
    frames = []
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    print("* done recording")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


if __name__ == '__main__':
  p1 = Process(target=video)
  p1.start()
  p2 = Process(target=audio)
  p2.start()
  p1.join()
  p2.join()