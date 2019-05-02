# Dictionary-Application
This is a GUI based dictionary application that displays information sourced from oxford dictionary API.

##
Here, I developed an app using the tkinter GUI module that provides various types of information that you might get about a word from a dictionary or thesaurus. The following widgets are in the design: an Entry box (for the word), Labels, a Scale slider bar, a Button, a Checkbutton, a Message output area, an OptionMenu, and Radiobuttons. By using these various widgets I am able to retrieve and display at least the following types of information:

1) Enter the word which will be looked up in the dictionary
2) See each of the different definitions of the word, including the part of speech for each
3) See the etymology of the word. 
4) See a phonetic spelling of the word for pronunciation.
5) Hear an audio pronunciation of the word
6) See a list of synonyms for the word
7) See a list of antonyms for the word
8) See a list of words that rhyme with the word
9) See example usage of the word in a sentence

The program can be modfied to display other word facts like its root parts, the plural of a word, other forms of the word, alternate spellings, etc.

The information displayed for an entered word is retrieved from any of a number of dictionary/thesaurus servers on the web by making url requests to an api. Some of these may return data in json format, others xml. But, here I chose to use only one API from Oxford Dictionary.
