import os
import speech_recognition as sr

def speak(text, voice):
    os.system("espeak -v {} '{}'".format(voice, text))

def listen():
    # Inizializza un riconoscitore vocale
    r = sr.Recognizer()

    # Usa il microfono come sorgente audio
    with sr.Microphone() as source:
        print("Dimmi qualcosa!")
        audio = r.listen(source)

    try:
        # Riconosci il testo dall'audio
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Non ho capito cosa hai detto.")
    except sr.RequestError as e:
        print("Impossibile completare la richiesta: {}".format(e))

if __name__ == '__main__':
    # Imposta la voce desiderata
    voice = 'en-scottish'

    # Inizia la conversazione
    while True:
        # Ascolta l'input vocale
        input_text = listen()
        print("Hai detto: {}".format(input_text))

        # Esegui la sintesi vocale in risposta
        response_text = "Hai detto: {}".format(input_text)
        speak(response_text, voice)
