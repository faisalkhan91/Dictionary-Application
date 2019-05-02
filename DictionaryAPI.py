# Importing system module

import json
import requests
import shutil
from pygame import mixer
import time

# Function Definitions


def url_request(get_word):

    # Application ID and Key

    app_id = 'f7e30bd9'
    app_key = 'eddb6a22f08f58e157a7dd26656cc2b6'

    language = 'en'
    word_id = get_word

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})

#    print("code {}\n".format(r.status_code))
#    print("text \n" + r.text)
#    print("json \n" + json.dumps(r.json()))

    json_dictionary = r.json()

#    print(json_dictionary["results"][0]["id"])

    return json_dictionary


def print_dictionary(word_data):

    print("The word is: \n", word_data["results"][0]["id"])
    print("Word Etymologies: \n", word_data["results"][0]["lexicalEntries"][0]["entries"][0]["etymologies"][0])
    print("Word definitions: \n", word_data["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]
    ["definitions"][0])
    print("Word definitions: \n", word_data["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][1]
    ["definitions"][0])

    pronounciaton = word_data["results"][0]["lexicalEntries"][0]["pronunciations"][0]["audioFile"]
    print(pronounciaton)

    # Reference
    # http://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
    sound = requests.get(pronounciaton, stream=True)
    with open('TempData\Sound.mp3', 'wb') as out_file:
        shutil.copyfileobj(sound.raw, out_file)
    del sound

    # References
    # http://stackoverflow.com/questions/20021457/playing-mp3-song-on-python
    # http://stackoverflow.com/questions/2936914/pygame-sounds-dont-play
    mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    mixer.music.load('TempData\sound.mp3')
    mixer.music.play()
    time.sleep(1)

    return
#############################################################################################

# Main Program

# word = input("Please enter the word to search for: ")
word = 'ace'

if word.isalpha():
    word_info = url_request(word)
#    print(word_info)

    print_dictionary(word_info)
else:
    print("Please enter a word!")
