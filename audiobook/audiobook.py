#importing the text to speech library pyttsx3
import pyttsx3

#giving the book location
book =open(r"book.txt")
book_text= book.readlines()
engine= pyttsx3.init()

print("Your audiobook is playing.....")
for i in book_text:
    engine.say(i)
    engine.runAndWait()
