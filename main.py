#THIS IS A TEST OF GITHUB COPILOT AND PYTHON 3

import time
from bs4 import BeautifulSoup as bs4
import requests 
import os 
import gtts 
import pygame 
import re 

cls = lambda: os.system("cls") 
cls()

#get url of qutoe to scrape
url = input("Enter a URL to scrape: ") 
#url = ""
#set default url if none is entered 
if url == "": 
    url = "https://www.reddit.com/r/shittymcsuggestions/comments/stp9qs/every_creeper_that_spawns_has_a_02147_chance_of/"

PAGE_TO_SCRAPE = requests.get(url) #what ever web page

if '404' in PAGE_TO_SCRAPE.url: 
    print("404 error") 
    quit()

soup = bs4(PAGE_TO_SCRAPE.text, "html.parser") 

#get the first h1 tag
timeout1 = 0 
while True: 
    if timeout1 == 10: 
        print("Error: Could not find the h1 tag") 
        print("\ncontinuing... anyway\n") #if it takes too long to find the h1 tag, it will continue anyway 
        time.sleep(1)
        h1 = "Error: Could not find the h1 tag" 
        break
    timeout1 += 1
    h1 = soup.find("h1")
    if h1 is None:
        #change the color of the text to red
        time.sleep(0.1)
        print("\033[91m" + "No h1 tag found" + "\033[0m")
        print("tried to find h1 tag " + str(timeout1) + " times") 
        print()
        continue
    if h1 is not None: 
        break

timeout2 = 0
while True:
    #find the first p tag
    if timeout2 == 10:
        print("Error: Could not find the p tag")
        print("\ncontinuing... anyway\n") #if it takes too long to find the p tag, it will continue anyway
        time.sleep(3)
        p = "Error: Could not find the p tag"
        break
    timeout2 += 1
    p = soup.find("p")
    if p is None:
        #change the color of the text to red
        time.sleep(0.1)
        print("\033[91m" + "No p tag found" + "\033[0m")
        print("tried to find p tag " + str(timeout2) + " times")
        print()
        continue
    if p is not None:
        break

#get an a tag with the data-click-id attribute of "subreddit"
timeout3 = 0
while True:
    if timeout3 == 10:
        print("Error: Could not find the subreddit link")
        print("\ncontinuing... anyway\n") #if it takes too long to find the subreddit link, it will continue anyway
        time.sleep(3)
        subreddit = "Error: Could not find the subreddit link"
        break
    timeout3 += 1
    subreddit = soup.find("a")
    if subreddit is None:
        #change the color of the text to red
        time.sleep(0.1)
        print("\033[91m" + "No subreddit link found" + "\033[0m")
        print("tried to find subreddit link " + str(timeout3) + " times")
        print()
        continue
    if subreddit is not None:
        break




#turn the h1 into the content of the tag
while True:
    try:
        h1 = h1.get_text() 
        break
    except:
        print("No h1 tag found")
        break
#turn the p into the content of the tag
while True:
    try:
        p = p.get_text()
        break
    except:
        print("No p tag found")
        break
#turn the subreddit into the content of the tag
while True:
    try:
        subreddit = subreddit.get_text()
        break
    except:
        print("No subreddit link found")
        break

print("\n"*3)
print("==========================================================")
print("subreddit: " + subreddit)
print("title: " + h1)
print("main story: " + p)
print("==========================================================")
print("\n"*1)
print("this will be saved to a mp3 file called 'title.mp3'")

script = "the title is "+h1+", and the main story is "+p+ ",that was from subreddit: "+subreddit #the script to be converted to mp3 and read

tts = gtts.gTTS(text=script, lang='en')  #convert the script to mp3
tts.save("title.mp3") 

pygame.mixer.init()
pygame.mixer.music.load("title.mp3") #load the mp3 file
pygame.mixer.music.play() #play the mp3 file


#press enter to exit
input("\n\nPress enter to exit")
print("saving...")
time.sleep(1)
