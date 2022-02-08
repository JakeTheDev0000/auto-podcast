import code
import os
import shutil
import sys
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup as bs4
from gtts import gTTS
from pygame import mixer

cls = lambda : os.system("cls")
cls()
try:
    user_set_url = str(input(">"))
    page_to_scrap = requests.get(user_set_url)
    soup = bs4(page_to_scrap.text, "html.parser")
except:
    print("error\nplease enter a link\n\n\n\nOH NO\nsystem has crashed please restart the APP\n\n\n\n\n\n\n")
def main():

    while True:
        title = soup.find("h1")
        print(title)
        if title == None:
            main()
        if title != None:
            cls()
            break


    try:
        title_text = title.text
    except:
        title_text = title.get_text()
    
    #title_text = "add flying in gamemode 0 haha"

    print(title_text)
    title_tts = gTTS(title_text)
    title_tts.save("main.mp3")

    mixer.init()
    mixer.music.load('main.mp3')
    mixer.music.play()

    time.sleep(5)
    cls()

    while True:
        print("the program has ended")
        print("close the program")
        time.sleep(1)
        cls()


main()
