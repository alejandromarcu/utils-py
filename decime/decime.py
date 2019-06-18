import sys
from lxml import html
import requests
import os
from playsound import playsound
from shutil import copyfile
from tempfile import gettempdir
import time
import re

save_path = "C:\\Cucu\\tmp\\wiktionary"
is_az = re.compile("[a-zA-Z]*")
lang = "Ru"


def get_audio_from_wiktionary(lang, word):
    url = "https://commons.wikimedia.org/w/index.php?title=File%3A{}-{}.ogg".format(lang, word)

    page = requests.get(url)
    tree = html.fromstring(page.content)

    download = tree.xpath('//a[@title="Download file"]')
    if not download:
        return None

    download_link = download[0].get("href")

    r = requests.get(download_link, allow_redirects=True)

    return r.content

while True:
    word = input("Word: ")

    if word == "x":
        break

    if is_az.match(word).span() == (0, 0):
        lang = "Ru"
        no_accents = word.encode().replace(b'\xcc\x81',b'').decode()
        if word != no_accents:
            word = no_accents
            print("Accents removed: " + word)
    else:
        lang = "En-us"
        word = word.lower()

    audio = get_audio_from_wiktionary(lang, word)
   
    if not audio:
        print("Can't find the entry for {}".format(word))
        continue

    filename = "{}\\{}.mp3".format(save_path, word)
    with open(filename, 'wb') as file:
        file.write(audio)

    tmp_file = os.path.join(gettempdir(), "wiktionary_{}_tmp.mp3".format(int(time.time())))
    copyfile(filename, tmp_file)
    playsound(tmp_file, True)
    os.unlink(tmp_file)
    
    print("Saved {}".format(filename))
    
