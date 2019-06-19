import sys
from lxml import html
import requests
import os
from playsound import playsound
from shutil import copyfile
from tempfile import gettempdir
import time
import re

script_path = os.path.dirname(sys.argv[0])
save_path = os.path.join(script_path, "audio")
is_az = re.compile("[a-zA-Z]*")

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


if not os.path.exists(save_path):
    os.mkdir(save_path)


while True:
    word = input("Word: ")

    if word == "x":
        break

    if is_az.match(word).span() == (0, 0):
        lang = "Ru"
        no_accents = word.encode().replace(b'\xcc\x81', b'').decode()
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

    save_path_with_lang = os.path.join(save_path, lang)
    if not os.path.exists(save_path_with_lang):
        os.mkdir(save_path_with_lang)    
        
    filename = os.path.join(save_path_with_lang, word)
    filename += '.mp3'
    with open(filename, 'wb') as file:
        file.write(audio)

    tmp_file = os.path.join(gettempdir(), "wiktionary_{}_tmp.mp3".format(int(time.time())))
    copyfile(filename, tmp_file)
    playsound(tmp_file, True)
    os.unlink(tmp_file)
    
    print("Saved {}".format(filename))
    
