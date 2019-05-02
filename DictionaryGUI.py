#!/usr/local/bin/python3

from tkinter import *


def clr():
    try:
        word.set("")
    except ValueError:
        pass


root = Tk()
root.title("DictionaryAPP")
root.lift()
#root.minsize(550, 400)
root.configure(width=750, height=570, bg="white smoke")

# Label Frame
labelframe = LabelFrame(root, fg="red", font=14, text="Dictionary App")
labelframe.grid(rowspan=2, columnspan=6)

# Label
label_info = Label(labelframe, text="Enter a word to search for:")
label_info.grid(row=0, column=0, sticky="news")

# Entry Box
word = StringVar()
word_box = Entry(labelframe, textvariable=word)
word_box.grid(row=0, column=1, sticky="NEWS")

# Button - Search
search_button = Button(labelframe, text="Search", width=10, fg="Blue")
search_button.grid(row=0, column=2, sticky="NEWS")

# Button - Quit
quit_button = Button(labelframe, text="Quit", fg="Red", width=10, command=root.quit)
quit_button.grid(row=0, column=3, sticky="NEWS")

# Button - Clear
clear_button = Button(labelframe, text="Clear", fg="Green", width=10, command=clr)
clear_button.grid(row=0, column=4, sticky="NEWS")

# Label Frame
labelframe2 = LabelFrame(root, fg="Blue", font=10, text="Select:")
labelframe2.grid(rowspan=2, columnspan=6)

# Check Buttons
c1 = Checkbutton(labelframe2, text="Check_1")
c1.grid(row=10, column=0)
c2 = Checkbutton(labelframe2, text="Check_2")
c2.grid(row=10, column=1)
c3 = Checkbutton(labelframe2, text="Check_3")
c3.grid(row=10, column=2)
c4 = Checkbutton(labelframe2, text="Check_4")
c4.grid(row=10, column=3)
c5 = Checkbutton(labelframe2, text="Check_5")
c5.grid(row=10, column=4)
c6 = Checkbutton(labelframe2, text="Check_6")
c6.grid(row=10, column=5)
c7 = Checkbutton(labelframe2, text="Check_7")
c7.grid(row=10, column=6)

# Label Frame
labelframe3 = LabelFrame(root, fg="Brown", font=10, text="Output")
labelframe3.grid(rowspan=2, columnspan=6)

# Message Box
output = StringVar()
output.set("This is my sample output text")
outbox = Message(labelframe3, textvariable=output)
outbox.grid(row=0, column=0, sticky=NSEW)

# Scale/Slider Bar
font = Scale(root, from_=0, to=200, orient=HORIZONTAL)
font.grid(row=6, column=5, sticky="NEWS")

# Radio Buttons
radio1 = Radiobutton(root, text="Option 1", value=1)
radio1.grid(row=6, column=0, sticky="NEWS")
radio2 = Radiobutton(root, text="Option 2", value=1)
radio2.grid(row=6, column=1, sticky="NEWS")

optionList = ('train', 'plane', 'boat')
option_menu = OptionMenu(root, *optionList)
option_menu.grid(row=6, column=2, sticky="NEWS")

root.mainloop()
