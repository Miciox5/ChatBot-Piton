import os

def speak(text):
    os.system('espeak "{}"'.format(text))

while True:
    phrase = input("Say something: ")
    speak(phrase)
