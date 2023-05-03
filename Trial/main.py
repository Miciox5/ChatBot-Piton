import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english')
print(engine.getProperty('voice'))
engine.say("Ciao, Mondo!")
engine.runAndWait()
