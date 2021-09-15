import streamlink
import subprocess
import time
import sys
import requests
import os
import json
import datetime
import getopt
from multiprocessing import Process
import shutil
from pynput.keyboard import Key, Controller


class TwitchRecorder:
    def __init__(self):
        self.projectFolder_Path = '/Users/TaW/Documents/GitHub/LiveTwitchRecording/'
        self.ffmpeg_path = '/Users/TaW/Documents/GitHub/LiveTwitchRecording/ffmpeg-20210728-0068b3d0f0-win64-static/bin/ffmpeg.exe'

        self.username = "qcoat"
        self.quality = "360p"

        self.filename = self.username+"_"+self.quality+".mp4"
        self.temp_RecordFile = ""
        self.streamerFolderPath = "/Users/TaW/Documents/GitHub/LiveTwitchRecording/" + self.username

    

    def RecordStream(self):   
        while True:

            self.temp_RecordFile = self.filename
            subprocess.call(["streamlink", "twitch.tv/" + self.username, self.quality, "-o", self.temp_RecordFile , "-t" , "10 input"])

    

    def SortFolder(self):
        isExist = os.path.exists(self.streamerFolderPath) 
        if  isExist == False:
            os.mkdir(self.streamerFolderPath)
        else:
            print("There is already a file for this streamer.")

        while True:
            time.sleep(10)
            if(os.path.exists(self.projectFolder_Path+self.filename) is True):
                try:
                    subprocess.call([self.ffmpeg_path, '-err_detect', 'ignore_err', '-i', self.projectFolder_Path+self.filename, '-c', 'copy', os.path.join(self.streamerFolderPath, datetime.datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss")+self.filename)])
                    os.remove(self.projectFolder_Path+self.filename)

                    # fo = open(self.projectFolder_Path+self.filename, "wb")
                    # fo.close()
                    # keyboard = Controller()

                    # print ("Name of the file: ", fo.name)
                    # keyboard.press("q")
                    # keyboard.release("q")
                    # Close opend file
                except Exception as e:
                    print(e)
            else:
                print("Skip fixing. File not found.")

        # os.rename(self.projectFolder_Path+self.filename, self.streamerFolderPath+"/"+datetime.datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss")+self.filename)


        


    

if __name__ == '__main__':
    twitch_recorder = TwitchRecorder()
    p1 = Process(target=twitch_recorder.RecordStream)
    p1.start()
    p2 = Process(target=twitch_recorder.SortFolder)
    p2.start()
    p1.join()
    p2.join()