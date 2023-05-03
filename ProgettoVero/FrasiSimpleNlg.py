from simplenlg.framework import *
from simplenlg.realiser.english import *
from simplenlg.features import *
import random
import time

#3)GENERAZIONE, Parte della generazione del linguaggio attraverso simpleNLG
#Per generare il lessico inglese, per formare le frasi in modo grammaticalmente corretto
lexicon = Lexicon.getDefaultLexicon()
nlgFactory = NLGFactory(lexicon)
realiser = Realiser(lexicon)

def FraseIniziale(n):
    if(n == 0):
        array = []
        p1 = nlgFactory.createClause("You", "be here") #Funzione che crea la frase prendendo come soggetto you, verbo be 
        p1.setPlural(True) #setta il verbo al plurale 
        p2 = nlgFactory.createClause("you", "learn", "the subtle science and exact art of potion-making")
        p2.setFeature(Feature.MODAL, "have to") 
        p2.setFeature(Feature.COMPLEMENTISER,"because") #creiamo la frase suboordinata causale 
        p1.addComplement(p2) #uniamo la suboordinata alla frase principale
        p3 = nlgFactory.createClause("tell me", "your name")
        p3.addFrontModifier("Now") #Con questa funzione aggiungiamo il modificatore che sta all'inizio della frase 
        p3.setFeature(Feature.COMPLEMENTISER, "to me") #realizziamo in questo modo il complemento di termine 
        p3.setPlural(True)
        a = realiser.realiseSentence(p1)
        array.append(a)
        a = realiser.realiseSentence(p3)
        array.append(a)
        return array
    elif(n == 1):
        array = []
        p1 = nlgFactory.createClause()
        p1.setPlural(True)
        p1.addFrontModifier("Here")
        p1.addPostModifier("foolishly,")
        p1.setVerb("do not wave")
        p1.setComplement("the wand")
        p1.setSubject("you")
        p2 = nlgFactory.createClause()
        p2.setSubject("you")
        p2.addFrontModifier("many of")
        verb = nlgFactory.createVerbPhrase("will believe")
        verb.addModifier("hardly")
        p2.setVerb(verb)
        p2.setComplement("in magic")
        p1.addPostModifier(p2)
        p3 = nlgFactory.createClause()
        p3.setSubject("you")
        p3.setVerb("are")
        p3.setComplement("one of these")
        p3.setPlural(True)
        p3.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
        p4 = nlgFactory.createClause("let's","find out")
        p4.setPlural(True)
        p5 = nlgFactory.createClause()
        p5.setVerb("be")
        p5.setComplement("your name")
        p5.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.WHAT_SUBJECT)
        p5.setPlural(True)
        a = realiser.realiseSentence(p1)
        array.append(a)
        a = realiser.realiseSentence(p2)
        array.append(a)
        a = realiser.realiseSentence(p3)
        array.append(a)
        a = realiser.realiseSentence(p4)
        array.append(a)
        a = realiser.realiseSentence(p5)
        array.append(a)
        return array
    elif(n == 2):
        array = []
        p1 = nlgFactory.createClause()
        p1.setPlural(True)
        p1.setSubject("I")
        p1.setVerb("can teach")
        p1.setComplement("you")
        p1.setComplement("how to bottle")
        p1.addPostModifier("fame")
        p2 = nlgFactory.createClause()
        p2.setVerb("brew")
        p2.setComplement("glory")
        p2.setPlural(True)
        p3 = nlgFactory.createClause()
        p3.setFrontModifier("even")
        p3.setVerb("stopper")
        p3.setComplement("death..")
        c = nlgFactory.createCoordinatedPhrase(p1, p2)
        c.addCoordinate(p3)
        p4 = nlgFactory.createClause()
        #p4.setPlural(True)
        p4.addFrontModifier("unless")
        p4.setSubject("you")
        p4.setVerb("be")
        p4.setComplement("an idiot")
        p5 = nlgFactory.createClause()
        p5.setPlural(True)
        p5.setComplement("all my students")
        p5.addFrontModifier("just")
        p5.setVerb("like")
        p5.addPostModifier("are")
        p4.addPostModifier(p5)
        p6 = nlgFactory.createClause()
        p6.setSubject("you")
        p6.setVerb("be")
        p6.setComplement("one of these")
        p6.setPlural(True)
        p6.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
        p7 = nlgFactory.createClause()
        p7.setVerb("be")
        p7.setComplement("your name")
        p7.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.WHAT_SUBJECT)
        p7.setPlural(True)
        a = realiser.realiseSentence(c)
        array.append(a)
        a = realiser.realiseSentence(p4)
        array.append(a)
        a = realiser.realiseSentence(p6)
        array.append(a)
        a = realiser.realiseSentence(p7)
        array.append(a)
        return array
    # Well Sara, let's see if you are worthy of your fame. Let's begin the questioning.

def fraseIntro(name):
    array = []
    p1 = nlgFactory.createClause()
    p1.setPlural(True)
    p1.addFrontModifier("Well")
    p1.setSubject(name)
    p1.setVerb("let's see")
    p1.setComplement("if")
    p2 = nlgFactory.createClause()
    p2.setPlural(True)
    p2.setSubject("you")
    p2.setVerb("be worthy")
    p2.setComplement("of your fame")
    p3 = nlgFactory.createClause()
    p3.setPlural(True)
    p3.setVerb("let's begin")
    p3.setComplement("the questioning")
    p1.addPostModifier(p2)
    a = realiser.realiseSentence(p1)
    array.append(a)
    a = realiser.realiseSentence(p3)
    array.append(a)
    return array

def questionTrabocchetto(pozione_corrente, ingrediente_scelto):
    p = nlgFactory.createClause();
    p.setSubject(pozione_corrente)
    p.setVerb("contain")
    p.setObject(ingrediente_scelto)
    p.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
    domanda_fatta = realiser.realiseSentence(p)
    return domanda_fatta

def questionPotion(pozione_corrente):
    # TEXT-PLAN
    p = nlgFactory.createClause()
    p.setSubject("ingredients")
    p.setVerb("be contained")
    p.setObject(pozione_corrente)
    # SENTENCE-PLAN
    p.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.WHAT_SUBJECT)
    domanda_fatta = realiser.realiseSentence(p)
    return domanda_fatta

def questionIngredient(ingrediente_scelto):
    p = nlgFactory.createClause()
    p.setSubject("you")
    p.setVerb("can find")
    p.setObject(ingrediente_scelto)
    p.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.WHERE)
    domanda_fatta = realiser.realiseSentence(p);
    return domanda_fatta

def rispIngGiaDetti():
    p2 = nlgFactory.createClause()
    p2.addFrontModifier("But")
    p2.setSubject("you")
    verb = nlgFactory.createVerbPhrase("say")
    verb.setFeature(Feature.TENSE, Tense.PAST)
    verb.addModifier("already")
    p2.setVerb(verb)
    p2.addPostModifier("that")
    response = realiser.realiseSentence(p2)
    return response

def rispIngMancanti():
    p1 = nlgFactory.createClause("This", "be not enough!")
    p2 = nlgFactory.createClause("I", "have expected", "it.")
    p2.setFeature(Feature.MODAL, "should")
    p3= nlgFactory.createClause("You", "understand", "the art of potion")
    p3.setFeature(Feature.MODAL, "can")
    p3.setFeature(Feature.NEGATED, True)
    p4 = nlgFactory.createClause()
    p4.setVerb("let's change")
    p4.setObject("the question")
    p4.setFeature(Feature.FORM, Form.IMPERATIVE)
    p3.addPostModifier(p4)
    p2.addPostModifier(p3)
    p1.addPostModifier(p2)
    response = realiser.realiseSentence(p1)
    return response

def rispTuttiIng():
    arr=[]
    p = nlgFactory.createClause("beginner's luck")
    p.addFrontModifier("Classic")
    p1 = nlgFactory.createClause("this potion", "be")
    p1.setFeature(Feature.TENSE, Tense.PAST)
    p1.addPostModifier("too easy.")
    p2 = nlgFactory.createClause("Let's see")
    p3 = nlgFactory.createClause("you","answer", "the next question")
    p3.setFeature(Feature.MODAL, "can")
    p3.addFrontModifier("if")
    p3.addPostModifier("as well")
    p2.addPostModifier(p3)
    p1.addPostModifier(p2)
    p.addPostModifier(p1)
    response = realiser.realiseSentence(p)
    arr.append(response);
    p4= nlgFactory.createClause("You", "be", "unbearable know-it-all")
    p4.setPlural(True)
    response2=realiser.realiseSentence(p4)
    arr.append(response2);
    return random.choice(arr)

def chiediIng():
    p1 = nlgFactory.createClause("tell me", "all ingredients", "that you know")
    p1.addFrontModifier("Fantastic!")
    p1.setPlural(True)
    response = realiser.realiseSentence(p1)
    return response

def chiediIngPoz(poz):
    p = nlgFactory.createClause("The potion", "be", poz)
    p.setFeature(Feature.TENSE, Tense.PAST)
    print(realiser.realiseSentence(p))
    time.sleep(1)
    p1 = nlgFactory.createClause("tell me", "all ingredients", "of that")
    p1.setPlural(True)
    response = realiser.realiseSentence(p1)
    return response

def chiediAltriIng():
    p = nlgFactory.createClause("you", "tell", "others")
    p.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
    p.setFeature(Feature.MODAL, "can")
    response = realiser.realiseSentence(p)
    return response

#Funzioni che generano le risposte di Piton
def rispPitonNeg(tag):
    if(tag == "ing1"):
        p = nlgFactory.createClause("ingredients")
        p.addFrontModifier("Some")
        p.setVerb("be correct")
        p.setPlural(True)
        p.addComplement("but not all")
    if(tag=="ing2"):
        p = nlgFactory.createClause("ingredient")
        p.setVerb("be correct")
        p.addFrontModifier("This")
        p.setFeature(Feature.NEGATED, True)
        print(realiser.realiseSentence(p))
        time.sleep(1)
        p = nlgFactory.createClause("you", "be lukier")
        p.setPlural(True)
        p.setFeature(Feature.TENSE, Tense.FUTURE)
        p.addFrontModifier("Maybe")
        p.addComplement("with the next ones")
    if(tag=="ing3"):
        p = nlgFactory.createClause("ingredients")
        p.setVerb("be correct")
        p.setPlural(True)
        p.addFrontModifier("All")
        p.setFeature(Feature.NEGATED, True)
        p.addComplement("muggle.")
        print(realiser.realiseSentence(p))
        time.sleep(1)
        p = nlgFactory.createClause("You", "waste", "my time")
        p.setPlural(True)
        p.setFeature(Feature.PROGRESSIVE, True)
    if(tag == "ing"):
        p = nlgFactory.createClause()
        subj = nlgFactory.createNounPhrase("questioning")
        subj.setDeterminer("the")
        p.setSubject(subj)
        verb = nlgFactory.createVerbPhrase("go")
        p.setVerb(verb)
        p.addPostModifier("badly")
    elif(tag == "poz"):
        p = nlgFactory.createClause()
        p.setSubject("Potion")
        p.setVerb("be correct")
        p.setFeature(Feature.NEGATED, True)
    elif(tag == "trab"):
        p = nlgFactory.createCoordinatedPhrase()
        p1 = nlgFactory.createClause()
        p1.setSubject("it")
        p1.setVerb("be wrong")
        p2 = nlgFactory.createClause()
        subj = nlgFactory.createNounPhrase("you")
        verb = nlgFactory.createVerbPhrase("tell me")
        objc = nlgFactory.createNounPhrase("ingredient")
        objc.setDeterminer("an")
        p2.setSubject(subj)
        p2.setVerb(verb)
        p2.setObject(objc)
        p2.addModifier("of this potion")
        p2.addPostModifier("at least")
        p.addCoordinate(p1)
        p.addCoordinate(p2)
    return realiser.realiseSentence(p)

def rispPitonTrab():
    p2 = nlgFactory.createClause()
    subj = nlgFactory.createNounPhrase("you")
    verb = nlgFactory.createVerbPhrase("tell me")
    objc = nlgFactory.createNounPhrase("ingredient")
    objc.setDeterminer("an")
    p2.setSubject(subj)
    p2.setVerb(verb)
    p2.setObject(objc)
    p2.addModifier("of this potion")
    p2.addPostModifier("at least")
    
    return realiser.realiseSentence(p2)

    
def rispPitonPos(tag):
    if(tag == "poz"):
        p1 = nlgFactory.createClause("Potion", "be correct")
        array= realiser.realiseSentence(p1)
        return array
    if(tag == "ing"):
        p1 = nlgFactory.createClause("Response", "be correct.")
        p2 = nlgFactory.createClause("you", "tell me", "all ingredients, yes or no")
        p2.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
        p2.setFeature(Feature.MODAL, "Can")
        p1.addPostModifier(p2)
        array = realiser.realiseSentence(p1)
        return array
    if (tag == "ing1"):
        p1 = nlgFactory.createClause("ingredient", "be correct")
        p1.addFrontModifier("This")
        resp = realiser.realiseSentence(p1)
        return resp
    if (tag == "ing2"):
        p1 = nlgFactory.createClause("you", "be lucky")
        p1.setPlural(True)
        p1.addFrontModifier("Well,")
        p1.setFeature(Feature.TENSE, Tense.PAST)
        print(realiser.realiseSentence(p1))
        time.sleep(1)
        p1 = nlgFactory.createClause("ingredients", "be correct")
        p1.setPlural(True)
        p1.addFrontModifier("These")
        resp = realiser.realiseSentence(p1)
        return resp

#Parte che permette di effettuare la Back-Strategy
def BackStrategy(tentativo):
    if(tentativo == 0):
        p = nlgFactory.createClause("You", "show up")
        p.setFeature(Feature.TENSE, Tense.PAST)
        s = nlgFactory.createNounPhrase("You")
        s.setFeature(Feature.ELIDED, True)
        v = nlgFactory.createClause(s, "waste", "my time")
        v.setPlural(True)
        v.setFeature(Feature.COMPLEMENTISER, "to")
        p.addComplement(v)
        d = realiser.realiseSentence(p)
        print(d)
        time.sleep(1.5)
        f = nlgFactory.createClause("you", "be sure")
        f.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
        f.setPlural(True)
        print(realiser.realiseSentence(f))
        time.sleep(0.5)
        f1 = nlgFactory.createClause(s, "Try")
        f1.setPlural(True)
        f2 = nlgFactory.createClause(s, "tell me", "one")
        f2.setPlural(True)
        f2.setFeature(Feature.COMPLEMENTISER, "to")
        f1.addComplement(f2)
        default = realiser.realiseSentence(f1)
    if(tentativo == 1):
        n = [0,1,2]
        m = random.choice(n)
        if(m == 0):
            defa = nlgFactory.createClause("I", " do not understand", "what you say")
            defa.addPostModifier("muggle")
            default = realiser.realiseSentence(defa)
        if(m == 1):
            defa = nlgFactory.createClause("muggle", "understand", "my question")
            defa.addFrontModifier("Stupid")
            defa.setFeature(Feature.TENSE, Tense.PAST)
            defa.setFeature(Feature.NEGATED, True)
            print(realiser.realiseSentence(defa))
            time.sleep(1)
            defa1 = nlgFactory.createClause("I", "waste", "my time")
            defa1.setFeature(Feature.MODAL, "have to")
            defa1.addFrontModifier("Now")
            s=nlgFactory.createNounPhrase("I")
            s.setFeature(Feature.ELIDED, True)
            defa2 = nlgFactory.createClause(s, "repeat", "it")
            defa2.setFeature(Feature.TENSE, Tense.FUTURE)
            defa2.setFeature(Feature.COMPLEMENTISER, "and")
            defa1.addComplement(defa2)
            default=realiser.realiseSentence(defa1)
            default=realiser.realiseSentence(defa1)
        if(m == 2):
            defa = nlgFactory.createClause("You", "be listen", "my question")
            defa.setFeature(Feature.NEGATED, True)
            defa.setPlural(True)
            defa.setFeature(Feature.TENSE, Tense.PAST)
            print(realiser.realiseSentence(defa))
            time.sleep(1)
            defa1= nlgFactory.createClause("I", "repeat", "it")
            defa1.addPostModifier("for the last time")
            default = realiser.realiseSentence(defa1)
#Hai esaurito la mia pazienza e tutte le tue possibilità, cambiamo domanda
    if(tentativo == 2):
        defa = nlgFactory.createClause("You", " have exhausted", "my patience")
        defa.addPostModifier("muggle")
        defa1 = nlgFactory.createClause("You", " have finish", "all possibilities.")
        defa.setPlural(True)
        defa1.setPlural(True)
        c = nlgFactory.createCoordinatedPhrase(defa, defa1)
        default = realiser.realiseSentence(c)
    return default

def controlloIngPos():
    p1 = nlgFactory.createClause("tell me", "all ingredients", "that you know")
    p1.addFrontModifier("Fantastic!")
    response = realiser.realiseSentence(p1);
    return response

def controlloIngNeg():
    p1 = nlgFactory.createClause("tell me", "the ones you know")
    p1.setPlural(True)
    response = realiser.realiseSentence(p1);
    return response

def approfIng():
    arr=[];
    p1 = nlgFactory.createClause("Tell me", "other ingredient")
    p1.setPlural(True)
    response1 = realiser.realiseSentence(p1)
    arr.append(response1);
    p2 = nlgFactory.createClause("Complete", "the list")
    p2.addModifier("of ingredient")
    response2 = realiser.realiseSentence(p2)
    arr.append(response2);
    time.sleep(1)
    p = nlgFactory.createClause("you", "remember", "which one are missing")
    p.setPlural(True)
    p.setFeature(Feature.INTERROGATIVE_TYPE, InterrogativeType.YES_NO)
    response3 = realiser.realiseSentence(p)
    arr.append(response3);
    time.sleep(1)
    return random.choice(arr)

def commentoVoto(valutazione):
    if(valutazione >= 0 and valutazione <= 17):
        #La tua testa non ha il permesso di rimanere a Hogwarts nessuna parte del tuo corpo ha il permesso di andare ad Hogwarts4
        #Ovviamente sei bocciato
        p=nlgFactory.createClause("Your head", "have allowed to stay", "at Hogwarts")
        p.setPlural(True)
        p.setFeature(Feature.NEGATED, True)
        p1=nlgFactory.createClause("part of your body", "be allowed to go", "to Hogwarts")
        p1.setFeature(Feature.COMPLEMENTISER, "any")
        p.addComplement(p1)
        print(realiser.realiseSentence(p))
        time.sleep(1.5)
        p3= nlgFactory.createClause("you", "be rejected")
        p3.setPlural(True)
        p3.addFrontModifier("Obviously")
        print(realiser.realiseSentence(p3))
    if(valutazione >= 18 and valutazione <= 23):
        #Non sei proprio un babbano, ma dobbiamo ancora lavorare con te, sei promosso per poco
        v=nlgFactory.createVerbPhrase("be")
        v.addModifier("really")
        p=nlgFactory.createClause("you", v, "a muggle")
        p.setPlural(True)
        p.setFeature(Feature.NEGATED, True)
        s= nlgFactory.createNounPhrase("we")
        p1 = nlgFactory.createClause(s, "work", "with you")
        p1.setPlural(True)
        p1.setFeature(Feature.MODAL, "have to")
        p1.addPreModifier("still")
        p1.setFeature(Feature.COMPLEMENTISER, "but")
        p.addComplement(p1)
        print(realiser.realiseSentence(p))
        time.sleep(1)
        v1 = nlgFactory.createVerbPhrase("be promoted")
        p2 = nlgFactory.createClause("You", v1)
        p2.setPlural(True)
        v1.addModifier("briefly")
        p2.addPostModifier("whit", valutazione)
        print(realiser.realiseSentence(p2))
    if(valutazione >=24 and valutazione <=26):
        #Non è semplice affrontare una mia interrogazione, difficilmente si passa con successo, ma tu sei l'eccezione alla regola
        #A malincuore devo promuoverti con "valutazione"
        p=nlgFactory.createClause("It", "be")
        p.setFeature(Feature.NEGATED, True)
        p.addPostModifier("easy")
        s= nlgFactory.createClause("to deal", "my questions")
        s.setPlural(True)
        s.setFeature(Feature.COMPLEMENTISER, "")
        p.addComplement(s)
        print(realiser.realiseSentence(p))
        time.sleep(1)
        v=nlgFactory.createVerbPhrase("be")
        p1 = nlgFactory.createClause("It", v, "difficult")
        p2= nlgFactory.createClause("to pass")
        p2.addModifier("successfully")
        p3 = nlgFactory.createClause("you", "be", "the exception")
        p3.setPlural(True)
        p3.addComplement("to the role")
        p2.setFeature(Feature.COMPLEMENTISER, "")
        p2.addComplement(p3)
        p1.addComplement(p2)
        print(realiser.realiseSentence(p1))
        time.sleep(1)
        p4 = nlgFactory.createClause("I", "promoted", "you with")
        p4.setFeature(Feature.MODAL, "have to")
        p4.addFrontModifier("Reluctantly")
        p4.addPostModifier(str(valutazione))
        print(realiser.realiseSentence(p4))
    if(valutazione >= 27 and valutazione <= 30):
       #Contro ogni aspettativa hai appreso la vera essenza della magia, sei degno della tua fama, con un maestro come me era scontato
        p=nlgFactory.createClause("you", "learn", "the true essence of magic")
        p.addFrontModifier("against all odds")
        p.setPlural(True)
        p.setFeature(Feature.PERFECT, True)
        s= nlgFactory.createClause("you", "be worthy", "your fame")
        s.setPlural(True)
        s.setFeature(Feature.COMPLEMENTISER, "")
        p1 = nlgFactory.createClause("it", "be obvius", "with a teacher like me")
        p1.setFeature(Feature.TENSE, Tense.PAST)
        p1.setFeature(Feature.COMPLEMENTISER, "")
        s.addComplement(p1)
        p.addComplement(s)
        print(realiser.realiseSentence(p))
        time.sleep(1)
        p2= nlgFactory.createClause("you", "be promoted", "with")
        p2.addFrontModifier("Congratulation")
        p2.setPlural(True)
        p2.addPostModifier(str(valutazione))
        print(realiser.realiseSentence(p2))
      