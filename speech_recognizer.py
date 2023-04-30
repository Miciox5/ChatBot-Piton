import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Parla adesso")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio, language="it-IT")
    print(f"Hai detto: {text}")
except sr.UnknownValueError:
    print("Non ho capito")
except sr.RequestError as e:
    print(f"Richiesta fallita; {e}")
