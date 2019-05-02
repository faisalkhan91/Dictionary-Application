#!/usr/bin/python3

#############################################################################################
#                               Program by Mohammed Faisal Khan                             #
#                               00598949                                                    #
#                               mkhan8@unh.newhaven.edu                                     #
#############################################################################################

# Importing system module

import json
import requests
import shutil
from pygame import mixer
import time
from tkinter import *
import tkinter.font as tkf
import tkinter.messagebox

# Global variables
# standard red, green, blue (RGB) color triplet
color = [208, 200, 196]

# Function Definitions

# ############### Dictionary API Functions ###############


# Function call to get all the json formatted dictionaries making API calls.
def url_request(get_word):

    # Application ID and Key

    app_id = 'f7e30bd9'
    app_key = 'eddb6a22f08f58e157a7dd26656cc2b6'

    language = 'en'
    word_id = get_word

    # Try/Except clause to display error for failed API requests
    try:
        url_dictionary = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
        url_antonyms_synonyms = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' \
                                + word_id.lower() + '/synonyms;antonyms'
        url_rhymes = "http://rhymebrain.com/talk?function=getRhymes&word=" + word_id.lower()

        request_word = requests.get(url_dictionary, headers={'app_id': app_id, 'app_key': app_key})
        request_antonyms = requests.get(url_antonyms_synonyms, headers={'app_id': app_id, 'app_key': app_key})
        request_rhymes = requests.get(url_rhymes)

    #    print("code {}\n".format(r.status_code))
    #    print("text \n" + r.text)
    #    print("json \n" + json.dumps(r.json()))

        json_dictionary_word = request_word.json()
        json_dictionary_antonyms = request_antonyms.json()
        json_dictionary_rhymes = request_rhymes.json()

    #    print(json_dictionary["results"][0]["id"])

        return json_dictionary_word, json_dictionary_antonyms, json_dictionary_rhymes, get_word
    except:
        tkinter.messagebox.showerror("Server connection",
                                     "Error - unable to connect to server. Try again.")

# ############### Dictionary GUI Functions ###############


# Search button function call
def search(switch):

    output.set("")
    word = word_text.get()

    if word.isalpha():
        word_info, word_antonyms, word_rhymes, just_word = url_request(word)
        #    print(word_info)

        if switch == 0:
            return word_info
        elif switch == 1:
            return word_antonyms
        elif switch == 2:
            return word_rhymes
        elif switch == 3:
            return just_word

        print_default(word_info)

    else:
        output.set("Please input a valid word.")


# Clear button function call
def clr():
    try:
        word_text.set("")
    except ValueError:
        pass


# Part of Scroll Bar
def frame_configure(canvas_window):
    # Reset the scroll region to encompass the inner frame
    canvas_window.configure(scrollregion=canvas_window.bbox("all"))


# Default output of a word search
def print_default(information):

    output.set("")
    # Word Output
    label_word = Label(frame, font=customFont2, fg="gray", text="Searched:")
    label_word.grid(row=0, column=0, sticky="W")

    set_word = StringVar()
    set_word.set(information["results"][0]["id"])
    word_message = Message(frame, textvariable=set_word, width=500)
    word_message.grid(row=1, columnspan=5, sticky=W)
    # Definitions output
    label_definitions = Label(frame, font=customFont2, fg="gray", text="Definitions:")
    label_definitions.grid(row=2, column=0, sticky="W")

    set_definitions = StringVar()
    set_definitions.set(information["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0])
    definitions_message = Message(frame, textvariable=set_definitions, width=700)
    definitions_message.grid(row=3, columnspan=5, sticky=W)

    set_definitions2 = StringVar()
    set_definitions2.set(information["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][1]["definitions"][0])
    definitions2_message = Message(frame, textvariable=set_definitions2, width=700)
    definitions2_message.grid(row=4, columnspan=5, sticky=W)

    label_sentence = Label(frame, font=customFont2, fg="gray", text="Examples:")
    label_sentence.grid(row=5, column=0, sticky="W")
    # Sentence Examples
    set_examples = StringVar()
    set_examples.set(information["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["examples"][0]["text"])
    examples_message = Message(frame, textvariable=set_examples, width=700)
    examples_message.grid(row=6, columnspan=5, sticky=W)

    set_examples2 = StringVar()
    set_examples2.set(information["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][1]["examples"][0]["text"])
    examples2_message = Message(frame, textvariable=set_examples2, width=700)
    examples2_message.grid(row=7, columnspan=5, sticky=W)


# Check button function call to display Synonyms
def check_synonyms(synonyms):

    label_synonyms = Label(frame, font=customFont2, fg="gray", text="Synonyms:")
    label_synonyms.grid(row=8, column=0, sticky="W")

    set_synonyms = StringVar()
    set_synonyms.set(synonyms["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["subsenses"][1]["synonyms"]
                     [1]["text"])
    synonyms_message = Message(frame, textvariable=set_synonyms, width=700)
    synonyms_message.grid(row=9, columnspan=5, sticky=W)

    set_synonyms2 = StringVar()
    set_synonyms2.set(synonyms["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["subsenses"][1]["synonyms"]
                      [2]["text"])
    synonyms_message2 = Message(frame, textvariable=set_synonyms2, width=700)
    synonyms_message2.grid(row=10, columnspan=5, sticky=W)


# Check button function call to display Antonyms
def check_antonyms(antonyms):

    label_antonyms = Label(frame, font=customFont2, fg="gray", text="Antonyms:")
    label_antonyms.grid(row=11, column=0, sticky="W")

    set_antonyms = StringVar()
    set_antonyms.set(antonyms["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["antonyms"][0]["text"])
    antonyms_message = Message(frame, textvariable=set_antonyms, width=700)
    antonyms_message.grid(row=12, columnspan=5, sticky=W)

    set_antonyms2 = StringVar()
    set_antonyms2.set(antonyms["results"][0]["lexicalEntries"][1]["entries"][0]["senses"][0]["antonyms"][0]["text"])
    antonyms_message2 = Message(frame, textvariable=set_antonyms2, width=700)
    antonyms_message2.grid(row=13, columnspan=5, sticky=W)


# Check button function call to display Phonetics
def check_phonetics(phonetics):

    label_phonetic = Label(frame, font=customFont2, fg="gray", text="Phonetics:")
    label_phonetic.grid(row=14, column=0, sticky="W")

    set_phonetics = StringVar()
    set_phonetics.set(phonetics["results"][0]["lexicalEntries"][0]["pronunciations"][0]["phoneticSpelling"])
    phonetics_message = Message(frame, textvariable=set_phonetics, width=700)
    phonetics_message.grid(row=15, columnspan=5, sticky=W)


# Check button function call to display Rhymes
def check_rhymes(rhymes):

    label_rhyme = Label(frame, font=customFont2, fg="gray", text="Rhymes:")
    label_rhyme.grid(row=16, column=0, sticky="W")

    set_rhymes = StringVar()
    set_rhymes.set(rhymes[0]["word"])
    rhymes_message = Message(frame, textvariable=set_rhymes, width=700)
    rhymes_message.grid(row=17, columnspan=5, sticky=W)

    set_rhymes = StringVar()
    set_rhymes.set(rhymes[1]["word"])
    rhymes_message = Message(frame, textvariable=set_rhymes, width=700)
    rhymes_message.grid(row=18, columnspan=5, sticky=W)


# Check button function call to display Etymology/Word Origin
def check_etymology(etymology):

    label_etymology = Label(frame, font=customFont2, fg="gray", text="Etymology:")
    label_etymology.grid(row=19, column=0, sticky="W")

    set_etymology = StringVar()
    set_etymology.set(etymology["results"][0]["lexicalEntries"][0]["entries"][0]["etymologies"][0])
    etymology_message = Message(frame, textvariable=set_etymology, width=500)
    etymology_message.grid(row=20, columnspan=5, sticky=W)


# Sound button function call to play a pronunciation of a word
def play_sound(sound_info):

    pronunciation = sound_info["results"][0]["lexicalEntries"][0]["pronunciations"][0]["audioFile"]
    # print(pronunciation)

    # Reference
    # http://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
    sound = requests.get(pronunciation, stream=True)
    file = str('TempData\Sound_' + str(sound_info["results"][0]["id"]) + ".mp3")
    with open(file, 'wb') as out_file:
        shutil.copyfileobj(sound.raw, out_file)
    del sound

    # References
    # http://stackoverflow.com/questions/20021457/playing-mp3-song-on-python
    # http://stackoverflow.com/questions/2936914/pygame-sounds-dont-play
    mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    mixer.music.load(file)
    mixer.music.play()
    time.sleep(1)
    mixer.quit()


# Menu button function call to change System Application Font Styles
def change_font(app_font):
    customFont.configure(family=app_font)


# Menu button function call to change Output's Label Font Styles
def change_font2(app_font):
    customFont2.configure(family=app_font)


# Function call for the clock label
def tick():
    # get the current local time from the PC
    time_string = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    clock.config(text=time_string)
    clock.after(200, tick)


# Option button function call to display translations
def translations():

    labelframe5 = LabelFrame(root, fg="Purple", font=customFont, text="Translations")
    labelframe5.grid(row=3, column=0, sticky=NSEW)

    label_translation = Label(labelframe5, text="Translations")
    label_translation.grid(row=0, column=0, sticky="news")

    app_id = 'f7e30bd9'
    app_key = 'eddb6a22f08f58e157a7dd26656cc2b6'
    word_id = search(3)

    source_language = 'en'
    target_language = 'es'

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + source_language + '/' + \
          word_id.lower() + '/translations=' + target_language

    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    # Getting the translation dictionary
    translation_dictionary = r.json()

    label_translation2 = Label(labelframe5, width=10, text="English: ")
    label_translation2.grid(row=1, column=0, sticky="W")

    set_translations = StringVar()
    set_translations.set(translation_dictionary["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]
                         ["examples"][0]["text"])
    translations_message = Message(labelframe5, textvariable=set_translations, width=700)
    translations_message.grid(row=1, column=1, sticky=W)

    label_translation2 = Label(labelframe5, width=10, text="Spanish: ")
    label_translation2.grid(row=2, column=0, sticky="W")

    set_translations2 = StringVar()
    set_translations2.set(translation_dictionary["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]
                          ["examples"][0]["translations"][0]["text"])
    translations2_message = Message(labelframe5, textvariable=set_translations2, width=700)
    translations2_message.grid(row=2, column=1, sticky=W)

    label_translation2 = Label(labelframe5, width=10, text="English: ")
    label_translation2.grid(row=3, column=0, sticky="W")

    set2_translations = StringVar()
    set2_translations.set(translation_dictionary["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]
                          ["examples"][1]["text"])
    translations_message2 = Message(labelframe5, textvariable=set2_translations, width=700)
    translations_message2.grid(row=3, column=1, sticky=W)

    label_translation2 = Label(labelframe5, width=10, text="Spanish: ")
    label_translation2.grid(row=4, column=0, sticky="W")

    set2_translations2 = StringVar()
    set2_translations2.set(translation_dictionary["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]
                           ["examples"][1]["translations"][0]["text"])
    translations2_message2 = Message(labelframe5, textvariable=set2_translations2, width=700)
    translations2_message2.grid(row=4, column=1, sticky=W)


# Function call to convert RGB to HTML color code
def convert_color(color):

    return '#{:02X}{:02X}{:02X}'.format(color[0], color[1], color[2])


# Function to change the color of the widget
def show_color(value, index):

    # update the global color triplet
    color[int(index)] = int(value)
    # convert it to hex code
    hex_code = convert_color(color)
    search_button.configure(bg=hex_code)
    clear_button.configure(bg=hex_code)
    quit_button.configure(bg=hex_code)


# Slider function call to update the Red color
def update_red(value):
    show_color(value, 0)


# Slider function call to update the Green color
def update_green(value):
    show_color(value, 1)


# Slider function call to update the Blue color
def update_blue(value):
    show_color(value, 2)

#############################################################################################

# Main Program

# ################# Dictionary API Main #################

# ################# Dictionary GUI Main #################

# Root window
root = Tk()
root.title("DictionaryAPP")
root.lift()
# Min/Max Window size
root.minsize(567, 410)
root.maxsize(567, 600)
root.configure(width=750, height=570, bg="white smoke")

# Custom fonts
customFont = tkf.Font(family="Helvetica", size=14)
customFont2 = tkf.Font(family="Helvetica")

# ###### LABEL FRAMES
# Label Frame 1
labelframe = LabelFrame(root, fg="red", font=17, text="Dictionary App")
labelframe.grid(row=0, column=0, sticky=NSEW)
# Label Frame 2
labelframe2 = LabelFrame(root, fg="DodgerBlue4", font=customFont, text="Select")
labelframe2.grid(row=1, column=0, sticky=NSEW)
# Label Frame 3
labelframe3 = LabelFrame(root, fg="Tomato", font=customFont, text="Output")
labelframe3.grid(row=2, column=0, sticky=NSEW)
# Label Frame 4
labelframe4 = LabelFrame(root, fg="Goldenrod3", font=customFont, text="Options")
labelframe4.grid(row=4, column=0, sticky=NSEW)
# Label Frame 6
labelframe6 = LabelFrame(root, fg="Black", font=customFont, text="Color")
labelframe6.grid(row=5, column=0, sticky=NSEW)

# ###### TIME
# Reference
# http://stackoverflow.com/questions/15689667/digital-clock-in-status-bar-in-python-3-and-tkinter
clock = Label(labelframe4, font=('times', 14, 'bold'), width=9, bg='SystemButtonFace')
clock.grid(row=0, column=7, sticky=E+W)
tick()

# ###### CANVAS/FRAME/SCROLLBAR
# Reference
# http://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter
canvas = Canvas(labelframe3, borderwidth=0)
frame = Frame(canvas)
vsb = Scrollbar(labelframe3, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set, width=542, heigh=200)

vsb.grid(sticky=N+E+S, row=0, column=1)
canvas.grid(sticky=N+W+S, row=0, column=0)
canvas.create_window((4, 4), window=frame, anchor="nw", tags="frame")

frame.bind("<Configure>", lambda event, new_canvas=canvas: frame_configure(canvas))

# ###### LABELS
# Label
label_info = Label(labelframe, text="Enter a word to search for:")
label_info.grid(row=0, column=0, sticky="news")
label_info = Label(labelframe4, width=12, text="Translations:")
label_info.grid(row=0, column=1, sticky="NEWS")
# ###### BUTTONS
# Button - Search
search_button = Button(labelframe, text="Search", width=10, bg=convert_color(color), fg="Blue",
                       command=lambda: search(-1))
search_button.grid(row=0, column=2, sticky="NEWS")
# Button - Clear
clear_button = Button(labelframe, text="Clear", bg=convert_color(color), fg="Green", width=10, command=clr)
clear_button.grid(row=0, column=3, sticky="NEWS")
# Button - Quit
quit_button = Button(labelframe, text="Quit", bg=convert_color(color), fg="Red", width=10, command=root.quit)
quit_button.grid(row=0, column=4, sticky="NEWS")
# Sound - Button
photo_sound = PhotoImage(file="Images\Sound.gif")
sound_button = Button(labelframe4, text="Sound", fg="Black", width=25, height=25, image=photo_sound,
                      command=lambda: play_sound(search(0)))
sound_button.grid(row=0, column=0, sticky="EW")

# ###### RADIO BUTTONS
# Radio Buttons
radio1 = Radiobutton(labelframe4, text="ON", value=1, command=translations)
radio1.grid(row=0, column=2, sticky="EW")
radio2 = Radiobutton(labelframe4, text="OFF", value=0)
radio2.grid(row=0, column=3, sticky="EW")

# ###### CHECK BUTTONS
# Check Buttons
# Reference
# http://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in
var = IntVar()
c1 = Checkbutton(labelframe2, text="Synonyms", variable=var, command=lambda: check_synonyms(search(1)))
c1.grid(row=0, column=0)
var2 = IntVar()
c2 = Checkbutton(labelframe2, text="Antonyms", variable=var2, command=lambda: check_antonyms(search(1)))
c2.grid(row=0, column=1)
var3 = IntVar()
c3 = Checkbutton(labelframe2, text="Phonetics", variable=var3, command=lambda: check_phonetics(search(0)))
c3.grid(row=0, column=2)
var4 = IntVar()
c4 = Checkbutton(labelframe2, text="Rhymes", variable=var4, command=lambda: check_rhymes(search(2)))
c4.grid(row=0, column=3)
var5 = IntVar()
c5 = Checkbutton(labelframe2, text="Etymology/Origin", variable=var5, command=lambda: check_etymology(search(0)))
c5.grid(row=0, column=4)
# var6 = IntVar()
# c6 = Checkbutton(labelframe2, text="Etymology")
# c6.grid(row=0, column=5)

# ###### SLIDER BARS
# Scale/Slider Bar
# Reference
# http://stackoverflow.com/questions/43595249/python-tkinter-scale-lambda-function
red_slider = Scale(labelframe6, orient='horizontal', width=15, length=180, from_=0, to=255, command=update_red)
red_slider.grid(row=1, column=0)
green_slider = Scale(labelframe6, orient='horizontal', width=15, length=180, from_=0, to=255, command=update_green)
green_slider.grid(row=1, column=1)
blue_slider = Scale(labelframe6, orient='horizontal', width=15, length=180, from_=0, to=255, command=update_blue)
blue_slider.grid(row=1, column=2)

# ###### OPTION MENUS
# Option Menu
# Reference
# http://stackoverflow.com/questions/4072150/how-to-change-a-widgets-font-style-without-knowing-the-widgets-font-family-siz
optionList = ('Bookman Old Style', 'Comic Sans MS', 'Courier New', 'Helvetica', 'Impact', 'Lucida Sans Unicode',
              'Tahoma', 'Times New Roman', 'Verdana')
option_var = StringVar()
option_var.set("System Font")
option_menu = OptionMenu(labelframe4, option_var, *optionList, command=change_font)
option_menu.grid(row=0, column=4, sticky="EW")
optionList2 = ('Bookman Old Style', 'Comic Sans MS', 'Courier New', 'Helvetica', 'Impact', 'Lucida Sans Unicode',
               'Tahoma', 'Times New Roman', 'Verdana')
option_var2 = StringVar()
option_var2.set("Output Font")
option_menu2 = OptionMenu(labelframe4, option_var2, *optionList, command=change_font2)
option_menu2.grid(row=0, column=5, sticky="EW")

# ###### ENTRY BOXES
# Entry Box
word_text = StringVar()
word_box = Entry(labelframe, textvariable=word_text, width=29)
word_box.grid(row=0, column=1, sticky="NEWS")

# ###### MESSAGE BOXES
# Message Box
output = StringVar()
output.set("Click search for word information.")
outbox = Message(frame, textvariable=output, width=500)
outbox.grid(row=0, column=0, sticky=NSEW)

# Configuration for the widget to expand with the window
root.rowconfigure(0, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)

# Root window loop
root.mainloop()

#############################################################################################
#                                       End of Program                                      #
#############################################################################################
