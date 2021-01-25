"""A program to grab weekly lunch menu.

This program pulls the weekly lunch menu from the Moodle server,
collects the days of the week into variables (not needed anymore), and
prints the current day's menu. if it doesn't find that day's menu,
like if today is Saturday, it'll return a "day not found" message. It
speaks using Google TTS, since that's multiplatform, and is what the
students are used to hearing for information messages anyways.

"""

# imports
import argparse
import datetime
import os

import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from playsound import playsound

# setup
URL = "https://moodle.alassist.us/mod/page/view.php?id=1323"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
# Get content
content = soup.find(id="region-main")

# Grab each day (no longer needed)
# try:
#     monday = content.find(text="Monday").findNext("ul")
#     print(f"For Monday, you're having: {monday.text}")
# except (NameError, AttributeError):
#     monday = print("Monday not found.\n")

# try:
#     tuesday = content.find(text="Tuesday").findNext("ul")
#     print(f"For Tuesday, you're having: {tuesday.text}")
# except (NameError, AttributeError):
#     tuesday = print("Tuesday not found.\n")

# try:
#     wednesday = content.find(text="Wednesday").findNext("ul")
#     print(f"For Wednesday, you're having: {wednesday.text}")
# except (NameError, AttributeError):
#     wednesday = print("Wednesday not found. \n")

# try:
#     thursday = content.find(text="Thursday").findNext("ul")
#     print(f"For Thursday, you're having: {thursday.text}")
# except (NameError, AttributeError):
#     thursday = print("Thursday not found.\n")

# try:
#     friday = content.find(text="Friday").findNext("ul")
#     print(f"For Friday, you're having: {friday.text}")
# except (NameError, AttributeError):
#     friday = print("Friday not found.\n")

today = datetime.datetime.today()
todayF = today.strftime("%A")


def menu():
    try:
        global output
        output = content.find(text={todayF}).findNext("ul").text
    except (NameError, AttributeError):
        output = str(todayF) + " not found."
    return output


menu()

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--speak", help="Speak output", action="store_true")
args = parser.parse_args()

if args.speak == True:
    tts = gTTS("today, you're having: " + output)
    filename = 'temp.mp3'
    tts.save(filename)
    playsound(filename)
    os.remove(filename)  #remove temporary file
else:
    tts = "error."

if args.speak == False:
    try:
        print(f"Today, you're having: \n {output} \n Press Enter when done reading.")
        input()
    except (NameError, AttributeError):
        print("error, can't print menu.\n Press Enter when done reading.")
        input()

parser.parse_args()
