import os
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

except:
    # I DONT KNOW WHAT TO DO HERE. i tried to make it a function but then soup NEEDS to be globol so i put it globle BUT NOOOOOOoo aperently thats not globole and im losing my mine so now its just a BIG MASSIVE error and closeing the program. 
    print("error\nplease enter a link\n\n\n\nOH NO\nsystem has crashed please restart the APP\n\n\n\n\n\n\n")
def main():

    page_to_scrap = requests.get(user_set_url)
    soup = bs4(page_to_scrap.text, "html.parser")

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

    # this is only here for develment. THIS WILL NO BE HERE ON THE RELEASE
    while True:
        print("the program has ended")
        print("close the program")
        time.sleep(999)
        cls()


main()
