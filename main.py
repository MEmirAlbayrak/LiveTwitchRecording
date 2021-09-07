from selenium import webdriver
import time
from skimage.metrics import structural_similarity as ssim

import cv2
import numpy as np
import pyautogui

driver = webdriver.Chrome()


pattern = r'https:\/\/(.*)\.com\.tr'

site = "https://www.twitch.tv/thebausffs"
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