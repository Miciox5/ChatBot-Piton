import simplenlg
from simplenlg.framework import *
from simplenlg.lexicon import *
from simplenlg.realiser.english import *
from simplenlg.phrasespec import *
from simplenlg.features import *
import random
from dm.context_model import Intent


class ResponseGenerator:
    lexicon = Lexicon.getDefaultLexicon()
    nlgFactory = NLGFactory(lexicon)
    realiser = Realiser(lexicon)

    def __init__(self) -> None:
        super().__init__()

    def evaluate(self, complete, matches):
        return int(complete * (sum(matches) / len(matches)))

    def initiate_exam(self, potion):
        return "Mr Potter, let's see if you deserve the fame you have.\nTell me the ingredients for " + potion + " potion"

    # per risposte parzialmente giuste (o mancano ingredienti o alcuni sono giusti e altri no)
    def clarify(self, data_frame, ingredient=None, matched=None, repeated=None):
        intent = data_frame['intent'].values[-1]
        expected = data_frame['expected'].values[-1]
        #print('repeated: ', repeated)
        if matched:
            feedback = ['Good job, ',
                        'So far so good Mr Potter, ',
                        'Curious, ',
                        'You are right, just this once, ',
                        'Good work, it was just luck '][random.randrange(4)]
        else:
            feedback = ['Too bad! It is clear that fame is not everything, ',
                        'You are wrong as usual, ',
                        'Nice try but of course you are wrong. '][random.randrange(3)]

        if intent == Intent.INGREDIENTS:
            answer = ['but I think you might be forgetting some ingredients. Hurry up, don\'t waste my time ',
                      'but You still have {} ingredients to go. '.format(len(expected)),
                      'but you should tell me some more ingredients. '][random.randrange(3)]
            if repeated:
                answer = 'Please don\'t repeat yourself. '
                return answer
            return feedback + answer

        elif intent == Intent.Y_N_INGREDIENT:
            answer = ['Mr. Potter, do you think {} is an ingredient of this potion?'.format(ingredient),
                      'Can you tell me if {} is present in this potion?'.format(ingredient)][random.randrange(2)]
            return feedback + answer

        else:
            ing = self.nlgFactory.createNounPhrase(ingredient)
            ing.addPreModifier('sure about')
            clause = self.nlgFactory.createClause('you', 'be', ing)
            clause.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
            return str(self.realiser.realise(clause))

    # per risposte giuste
    def eval(self, complete, matches):
        #print('complete {}'.format(complete))
        #print('matches {}'.format(matches))
        evaluation = self.evaluate(complete, matches[1:-1])

        if evaluation == 100:
            answer = ['It seems like you have gotten all the ingredients right Potter, but it was all luck. ',
                      'It is easy to see that nearly six years of magical education have not been wasted on you, Potter. ',
                      'Potter, I definitely was not expecting this result from you. ',
                      'You guessed all the ingredients Potter, after all I would expect nothing less from a celebrity like you. ',
                      'Well, well Potter. It seems like your friendship with miss Granger is paying off after all. '][random.randrange(5)]
        elif evaluation > 50:
            answer = [
                'Nice try Potter, you passed this exam. ',
                'Your exam wasn\'t too bad, Potter. Of course I would expect something more from a know-it-all like you.',
                'You passed the exam Potter, though I wouldn\'t celebrate too much. This is still a bad result.'][random.randrange(3)]
        else:
            answer = ['I would\'ve expected nothing more from you Potter, I can see you were raised by muggles',
                      # 'Because of your irreverence, the house of Gryffindor lost {}'.format(100-evaluation),
                      'Because of your irreverence, the house of Gryffindor lost points',
                      'It\'s nice to see that nearly six years of magical education have been wasted on you, Potter.',
                      'You are just as useless as your father Potter, you failed this exam'][
                random.randrange(3)]
        answer += ' Your final evaluation for the Potion\'s class is ' + str(evaluation)
        return ['Out of all expectations, this exam is over.\n', answer, '.\nI have already spent enough time on you']

    # per risposte sbagliate
    def refusal(self):
        answer = ['Answers like this will cost some points to your House',
                  'How extraordinarily like your father you are, Potter. He too was exceedingly bad at potions',
                  'Mr Potter you better concentrate if you don\'t want me to take away points from Gryffindor',
                  'Mr Potter I remind you this is not Defence against the Dark Arts'][
            random.randrange(4)]
        answer += ', I suggest you tell me some real ingredients'
        return answer

    def greeting(self, potion):
        return "Potter, our new celebrity"

    def back_up_strategy(self):
        return "I do not understand what you are saying. Try again, Potter!!!"
