import pyttsx3


class TextToSpeech:

    def __init__(self) -> None:
        super().__init__()
        self._engine = pyttsx3.init()
        self._voices = self._engine.getProperty('voices')
        self._engine.setProperty('voice', self._voices[7].id)
        # self._engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel') # inserire qui la voce del personaggio Snape

    def say(self, sentence):
        if isinstance(sentence, list):
            print('Professor Snape: {}'.format(' '.join(sentence)))
            for i, elem in enumerate(sentence):
                if i == (len(sentence) - 1):
                    self._engine.setProperty('rate', 260)
                    self._engine.setProperty('volume', 1)
                self._engine.say(elem)
        else:
            print('Professor Snape: {}'.format(sentence))
            self._engine.say(sentence)
        self._engine.runAndWait()
