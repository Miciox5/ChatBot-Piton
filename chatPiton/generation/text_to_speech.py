import pyttsx3


class TextToSpeech:

    def __init__(self) -> None:
        super().__init__()
        self._engine = pyttsx3.init()
        self._voices = self._engine.getProperty('voices')
        self._engine.setProperty('voice', 'english')
        self._engine.setProperty('rate', 150)
        self._engine.setProperty('volume', 0.8)

    def say(self, sentence):
        if isinstance(sentence, list):
            print('Professor Snape: {}'.format(' '.join(sentence)))
            for i, elem in enumerate(sentence):
                if i == (len(sentence) - 1):
                    self._engine.setProperty('volume', 1)
                if 'Mr Potter' in sentence:
                    self.say_Mr_Potter()
                    sentence = sentence.replace('Mr Potter', '', 1)
                if 'Potter' in sentence:
                    self.say_Potter()
                    sentence = sentence.replace('Potter', '', 1)
                self._engine.say(elem)

        else:
            print('Professor Snape: {}'.format(sentence))
            if 'Mr Potter' in sentence:
                self.say_Mr_Potter()
                sentence = sentence.replace('Mr Potter', '', 1)
            if 'Potter' in sentence:
                self.say_Potter()
                sentence = sentence.replace('Potter', '', 1)
            self._engine.say(sentence)
        self._engine.runAndWait()

    def say_Potter(self):
        old_rate = self._engine.getProperty('rate')
        old_volume = self._engine.getProperty('volume')
        self._voices = self._engine.getProperty('voices')
        self._engine.setProperty('rate', 130)
        self._engine.setProperty('volume', 1)
        self._engine.say('Potter!')
        self._engine.setProperty('rate', old_rate)
        self._engine.setProperty('volume', old_volume)

    def say_Mr_Potter(self):
        old_rate = self._engine.getProperty('rate')
        old_volume = self._engine.getProperty('volume')
        self._voices = self._engine.getProperty('voices')
        self._engine.setProperty('rate', 100)
        self._engine.setProperty('volume', 1)
        self._engine.say('Mr Potter!')
        self._engine.setProperty('rate', old_rate)
        self._engine.setProperty('volume', old_volume)
