import subprocess
import sys
import time
import os
import datetime
from multiprocessing import Process
from pynput.keyboard import Key, Controller

# My own version for the recorder
# You can record twitch streamers live video with this script
# but i did t figure out how can i make ffmpeg record every 10sec and move new file to folder.

class TwitchRecorder:
    def __init__(self):
        self.projectFolder_Path = '/Users/TaW/Documents/GitHub/LiveTwitchRecording/'
        self.ffmpeg_path = '/Users/TaW/Documents/GitHub/LiveTwitchRecording/ffmpeg-20210728-0068b3d0f0-win64-static/bin/ffmpeg.exe'  # ffmpeg exe

        self.username = "sylchasie"
        self.quality = "best"

        self.filename = self.username+"_"+self.quality+".mp4"
        self.temp_RecordFile = ""
        self.streamerFolderPath = "/Users/TaW/Documents/GitHub/LiveTwitchRecording/" + self.username

    

    def RecordStream(self):   
        self.temp_RecordFile = self.filename
        subprocess.call(["streamlink", "twitch.tv/" + self.username, self.quality,"-o", self.temp_RecordFile])
            
            


    def SortFolder(self):
        isExist = os.path.exists(self.streamerFolderPath) 
        if  isExist == False:
            os.mkdir(self.streamerFolderPath)
        else:
            print("There is already a file for this streamer.")

        while True:
            time.sleep(5)
            if(os.path.exists(self.projectFolder_Path+self.filename) is True):
                try:
                    date = datetime.datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss")
                    os.system(self.ffmpeg_path+ " -sseof -4 -i " + self.projectFolder_Path+self.filename + " " + self.projectFolder_Path+"test"+self.filename)
                    subprocess.call([self.ffmpeg_path, '-err_detect', 'ignore_err', '-i', self.projectFolder_Path+"test"+self.filename, '-c', 'copy', os.path.join(self.streamerFolderPath, date+self.filename)])
                    os.remove(self.projectFolder_Path+"test"+self.filename)
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
    

