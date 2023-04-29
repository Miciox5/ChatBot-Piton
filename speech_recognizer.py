import speech_recognizer as sr

# get the index of your microphone
mic_index = None
for i, microphone_name in enumerate(sr.Microphone.list_microphone_names()):
    if "your_microphone_name" in microphone_name:
        mic_index = i
        break

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('Potter: ')
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    r.recognize_google(audio)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
