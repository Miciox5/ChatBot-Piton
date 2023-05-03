import time
import json 
import random
import FrasiSimpleNlg #file python per la generazione del linguaggio

#funzione che prende le pozioni dalla base di conoscenza rappresentata dal file json
def poz():
  pozioni = json.load(open("pozioni.json"))
  return pozioni

data = poz() #variabile per leggere il file json
frame_pozione = {} #frame per le pozioni
pozione_corrente = ""; #common ground
ingrediente_scelto="";
nomi_pozioni = list(data.keys()) #lista che prende i nomi delle pozioni dal file json
stringa_risposta="";
domanda_fatta="";
tag="";
currentIndex=-1;
frame_corrente = {}
ing = [];
risp_insicure = ["i do not know", "i don't know", "i do not remember", "i don't remember", "boh", "i do not say", "i don't say"]

indici=list(range(0, len(nomi_pozioni))) #funzione che fa una lista di numeri da 0 a len(nomi_pozioni)
#nel main quando richiamiamo createFrame() facciamo il controllo su questi array per vedere se continuare o meno
#(cioè per vedere quando abbiamo fatto le domande su tutti i frame (pozioni)

#Funzione che restituisce un array con tutti gli ingredienti delle tre pozioni 
def IngTot():
    global nomi_pozioni
    nomi_pozioni_totali = list(data.keys())
    lista_ingredienti_totali = [];
    for i in range(len(nomi_pozioni)):
        pozi = nomi_pozioni[i]
        for j in range(len(data[pozi])):
            lista_ingredienti_totali.append(data[pozi][j])
    return lista_ingredienti_totali

#Creazione del frame per controllare l'interrogazione
#La funzione restituisce il frame
def createFrame():
    global pozione_corrente
    global nomi_pozioni
    global indici;
    global currentIndex
    if(len(indici) != 1):
       currentIndex=random.choice(indici) #prende un frame a caso e setta il suo indice sulla variabile globale currentIndex
    else:
        currentIndex=indici[0] #prende il frame contenente l'ultima pozione rimasta 
    pozione_corrente = nomi_pozioni[currentIndex] 
    indici.remove(currentIndex);
    for i in range(len(data[pozione_corrente])):
        frame_pozione["name"] = pozione_corrente
        frame_pozione[data[pozione_corrente][i]] = False
    return frame_pozione


#Funzione che se richiamata setta di nuovo tutti gli ingredienti del frame corrente a False
def reset():
  global pozione_corrente;
  for i in range(len(data[pozione_corrente])):
    frame_pozione["name"] = pozione_corrente
    frame_pozione[data[pozione_corrente][i]] = False
  #print(frame_pozione)

#Funzione che restituisce il numero degli ingredienti della pozione che ha come argomento
def getDosi(pozione):
    dosi = len(data[pozione])
    return dosi

#Funzione che restituisce gli ingredienti della pozione che è stata scelta a caso
def findIngredients(pozione):
    global frame_corrente
    ingredienti_correnti = [];
    for i in range(len(data[pozione])):
        ingredienti_correnti.append(data[pozione][i])
    return ingredienti_correnti

#Funzione che prende gli ingredienti ancora a False
def getCountFalse(): #getCountFalse
    global frame_corrente 
    count = 0
    for i in range(len(data[pozione_corrente])):
        if(frame_pozione[data[pozione_corrente][i]] == False):
            count += 1
    return count  
#Funzione che restituisce una lista degli ingredienti corretti detti
def getCountTrue(): #getCountTrue
    global frame_corrente
    ing_true = [];
    for i in range(len(data[pozione_corrente])):
        if(frame_pozione[data[pozione_corrente][i]] == True):
            ing_true.append(frame_pozione[data[pozione_corrente][i]])
    return ing_true

#Funzione che estrapola le informazioni dal frame corrente (le risposte positive), memoria temporanea. Serve per creare una memoria (store())
def getKeyValueTrue():
  ingTrue=[]
  for key, value in frame_corrente.items():
    if (value == True):
      ingTrue.append(key);
  return ingTrue;

#Funzione che estrapola le informazioni dal frame corrente (le risposte negative), memoria temporanea. Serve per creare una memoria (store())
def getKeyValueFalse():
  ingFalse=[]
  for key, value in frame_corrente.items():
    if (value == False):
      ingFalse.append(key);
  return ingFalse;

#Funzione che restituisce la pozione in base all'ingrediente scelto random
def findPotion(ingrediente):
    for i in range(len(nomi_pozioni)):
        ingredienti_pozione = findIngredients(nomi_pozioni[i])
        if (ingrediente in ingredienti_pozione):
            return  nomi_pozioni[i]

#Funzioni che attraverso la libreria simpleNLG genera le diverse categorie di domande 
#Genera le domande a trabocchetto
def getQuestionsTrabocchetto():
  global domanda_fatta
  global ingrediente_scelto
  global pozione_corrente
  global stringa_risposta;
  #print(pozione_corrente);
  ingrediente_scelto="";
  ingrediente_scelto = random.choice(IngTot());
  #print(ingrediente_scelto)
  domanda_fatta = FrasiSimpleNlg.questionTrabocchetto(pozione_corrente, ingrediente_scelto)
  return domanda_fatta
  


#Genera le domande che chiedono gli ingredienti di una certa pozione
def getQuestionsPotion():
  global domanda_fatta
  global pozione_corrente
  global stringa_risposta;
  domanda_fatta = FrasiSimpleNlg.questionPotion(pozione_corrente)
  return domanda_fatta

    
#Genera le domande in cui si chiede in quale pozione si trova l'ingrediente nominato nella domanda 
def getQuestionsIngredient():
  global domanda_fatta
  global ingrediente_scelto
  global stringa_risposta;
  global pozione_corrente
  ingrediente_scelto="";
  ingrediente_scelto = random.choice(findIngredients(pozione_corrente))
  #print(ingrediente_scelto)
  domanda_fatta = FrasiSimpleNlg.questionIngredient(ingrediente_scelto)
  return domanda_fatta

#2)DM (Dialogue Manager),parte che fa partire il dialogo, gestisce le domande e controlla le risposte 

#Funzione genera le domande random
def queries():
    global pozione_corrente
    global ingrediente_scelto
    global domanda_fatta
    global stringa_risposta
    global tag;
    global vettDom
    global cambia
    domanda_fatta=""; #stringa che ci serve per riscrivere la domanda appena fatta
    tipi = ["domanda_ingrediente", "domanda_pozione", "domanda_trabocchetto"];
    tag ="";
    tag = random.choice(tipi)
    if(tag == "domanda_ingrediente"):
        domanda_fatta=getQuestionsIngredient()
    if(tag == "domanda_pozione"):
        domanda_fatta=getQuestionsPotion()
    if(tag == "domanda_trabocchetto"):
        domanda_fatta=getQuestionsTrabocchetto()
    stringa_risposta = input(domanda_fatta).lower()


#Funzione che analizza le risposte insicure dell'utente
def frs(stringa_risposta):
  global risp_insicure;
  flag=False;
  for i in range (len(risp_insicure)):
    if (risp_insicure[i] in stringa_risposta):
      flag=True;
  return flag;

#Funzione che riempie e aggiorna il frame corrente
def ctrlIngredientsPotion(pozione_corrente, stringa_risposta):
    global ing;
    global frame_corrente
    ripetizioni=False;
    count_giusti = 0;
    count_sbagliati = 0;
    count_tot = 0
    tot = IngTot();
    for i in range(1, len(ing)):
        if(ing[i] in stringa_risposta):
            count_giusti +=1;
            if(frame_corrente[ing[i]]==True):
                ripetizioni=True
            elif(frame_corrente[ing[i]]==False):
                frame_corrente[ing[i]]=True
    for i in range(len(tot)):
        if(tot[i] in stringa_risposta):
            count_tot+=1
    count_sbagliati = count_tot-count_giusti
    if(count_giusti == 1 and count_sbagliati == 0):
        print(FrasiSimpleNlg.rispPitonPos("ing1"))
        #print("This ingredient is correct")
    elif(count_giusti > 0 and count_sbagliati == 0):
        print(FrasiSimpleNlg.rispPitonPos("ing2"))
        #print("These ingredients are correct")
    if(count_giusti > 0 and count_sbagliati > 0):
        print(FrasiSimpleNlg.rispPitonNeg("ing1"))
    if(count_giusti == 0 and count_sbagliati ==1):
        print(FrasiSimpleNlg.rispPitonNeg("ing2"))
        #print("This ingredient is not correct")
    elif(count_giusti == 0 and count_sbagliati >0):
        print(FrasiSimpleNlg.rispPitonNeg("ing3"))
        #print("All ingredients are wrong")
    if(ripetizioni ==True and getCountFalse()!=0):
        print(FrasiSimpleNlg.rispIngGiaDetti())

#Funzione che  restituisce true se l'utente ha risposto si/no       
def ctrlYesNo(stringa_risposta):
    if ("yes" in stringa_risposta or "no" in stringa_risposta):
        flag=True;
    else:
      flag=False
    return flag;

#Funzione che restituisce True se l'utente non ha detto una pozione valida      
def ctrlValidPotion(stringa_risposta):
    flag=False;
    for i in range(len(nomi_pozioni)):
        if(nomi_pozioni[i]  in stringa_risposta):
            flag =True 
    return flag;

#Funzione che restituisce True se l'utente non ha detto un ingrediente valido   
def ctrlValidIngr(stringa_risposta):
    flag=False;
    tot=IngTot();
    for i in range(len(tot)):
        if(tot[i]  in stringa_risposta):
            flag =True 
    return flag;

#Funzione che controlla il dialogo nella situazione di risposta insicura
def ctrlIdont(domanda_fatta, stringa_risposta, tag):
  global pozione_corrente;
  if (tag== "ing"):
    domanda_fatta=FrasiSimpleNlg.BackStrategy(0);
  if (tag=="trab"):
    domanda_fatta=FrasiSimpleNlg.rispPitonTrab();
  if (tag=="poz"):
    domanda_fatta=FrasiSimpleNlg.chiediIngPoz(pozione_corrente);
  tenta=0;
  stringa_risposta=input(domanda_fatta).lower();
  ctrlIngredientsPotion(pozione_corrente, stringa_risposta);
  f=frs(stringa_risposta);
  while(f==False and tenta<2):
    if (getCountFalse()==0):
            break;
    domanda_fatta=FrasiSimpleNlg.approfIng();
    stringa_risposta=input(domanda_fatta).lower();
    ctrlIngredientsPotion(pozione_corrente, stringa_risposta);
    f=frs(stringa_risposta);
    tenta+=1;
  if(tenta == 1):
      print(FrasiSimpleNlg.BackStrategy(2))
  if (getCountFalse()==getDosi(pozione_corrente)):##detti nessuno
    print(FrasiSimpleNlg.rispPitonNeg("ing")); #NON CI SIAMO
  if (getCountFalse()==0): #detti tutti
    print( FrasiSimpleNlg.rispTuttiIng());
  elif (tenta>=2): ##tentativi finiti
    print(FrasiSimpleNlg.rispIngMancanti());
  return;
  
#Funzione che controlla il dialogo nella situazione di domanda trabocchetto  
def controlloDomandaTrabocchetto(domanda_fatta, stringa_risposta):
    global ingrediente_scelto;
    global pozione_corrente;
    poz_corretta=findPotion(ingrediente_scelto);
    flag=ctrlYesNo(stringa_risposta); 
    f=frs(stringa_risposta);
    if(f==True): #risposta insicura
      ctrlIdont(domanda_fatta, stringa_risposta, "trab")
      return;
    controllo=0;
    while (flag==False and controllo<2): #risposta si/no
        print(FrasiSimpleNlg.BackStrategy(1))
        stringa_risposta=input(domanda_fatta).lower()
        flag=ctrlYesNo(stringa_risposta);
        controllo+=1;
    if (flag==False):
        print(FrasiSimpleNlg.BackStrategy(2));
        return
    #è uscito dal while quindi stringa_risposta è si o no
    if ((poz_corretta==pozione_corrente and "yes" in stringa_risposta)or
        (poz_corretta!=pozione_corrente and "no" in stringa_risposta)):
        #ha risposto bene
        if ("yes" in stringa_risposta):
            for key, value in frame_corrente.items():
                if (key==ingrediente_scelto):
                    frame_corrente[key]=True;
        domanda_fatta=FrasiSimpleNlg.rispPitonPos("ing"); 
        stringa_risposta=input(domanda_fatta).lower();
        flag=ctrlYesNo(stringa_risposta);
        controllo=0;
        while (flag==False and controllo<2): #risposta si/no
            print(FrasiSimpleNlg.BackStrategy(1))
            stringa_risposta=input(domanda_fatta).lower()
            flag=ctrlYesNo(stringa_risposta);
            controllo+=1;
        if (flag== False):
            print(FrasiSimpleNlg.BackStrategy(2)) #i tentativi sono finiti
        #è uscito dal while quindi stringa_risposta è si o no  
        if ("yes" in stringa_risposta):
            domanda_fatta=FrasiSimpleNlg.controlloIngPos(); 
            stringa_risposta=input(domanda_fatta).lower();
            tentativi=0;
            f=frs(stringa_risposta)
            if (f==True): #risposta insicura
              ctrlIdont(domanda_fatta, stringa_risposta, "ing")
              return;
            ctrlIngredientsPotion(pozione_corrente, stringa_risposta)
            while (getCountFalse()!=0 and tentativi<2): #il frame non è completo ma i tentativi sono finiti
                if (getCountFalse()==0):
                    break;
                domanda_fatta=FrasiSimpleNlg.approfIng(); 
                stringa_risposta=input(domanda_fatta).lower();
                f=frs(stringa_risposta)
                if (f==True): #risposta insicura
                  ctrlIdont(domanda_fatta, stringa_risposta, "ing")
                  return;
                ctrlIngredientsPotion(pozione_corrente, stringa_risposta)
                tentativi+=1;
            if (getCountFalse()==getDosi(pozione_corrente)): #il frame non è riempito
                print(FrasiSimpleNlg.rispPitonNeg("ing"));
            if (getCountFalse()==0): #il frame è completo
                print( FrasiSimpleNlg.rispTuttiIng());
            elif (tentativi>=2): # i tentativi finiti
                print(FrasiSimpleNlg.rispIngMancanti());
        #risposta sbagliata
        if ("no" in stringa_risposta):
            domanda_fatta=FrasiSimpleNlg.controlloIngNeg();
            stringa_risposta=input(domanda_fatta).lower();
            tentativi=0;
            f=frs(stringa_risposta) #risposta insicura
            if (f==True):
              ctrlIdont(domanda_fatta, stringa_risposta, "ing")
              return;
            ctrlIngredientsPotion(pozione_corrente, stringa_risposta)
            while (getCountFalse()!=0 and tentativi<2): #frame non completo 
                if (getCountFalse()==0):
                    break;
                domanda_fatta=FrasiSimpleNlg.approfIng();
                stringa_risposta=input(domanda_fatta).lower();
                f=frs(stringa_risposta)
                if (f==True):
                  ctrlIdont(domanda_fatta, stringa_risposta, "ing")
                  return;
                ctrlIngredientsPotion(pozione_corrente, stringa_risposta)
                tentativi+=1;
            if (getCountFalse()==getDosi(pozione_corrente)):##detti nessuno
                print(FrasiSimpleNlg.rispPitonNeg("ing"));
            if (getCountFalse()==0): #detti tutti
                print( FrasiSimpleNlg.rispTuttiIng());
            elif (tentativi>=2): ##tentativi finiti
                print(FrasiSimpleNlg.rispIngMancanti());
    #risposta non compresa dal sistema
    else:    
        domanda_fatta=FrasiSimpleNlg.rispPitonNeg("trab"); 
        stringa_risposta=input(domanda_fatta).lower();
        tentativi=0;
        f=frs(stringa_risposta)
        if (f==True):
          ctrlIdont(domanda_fatta, stringa_risposta, "ing")
          return;
        ctrlIngredientsPotion(pozione_corrente, stringa_risposta)
        while (getCountFalse()!=0 and tentativi<2): #frame non completo
            if (getCountFalse()==0):
                break;
            domanda_fatta=FrasiSimpleNlg.approfIng();
            stringa_risposta=input(domanda_fatta).lower();
            f=frs(stringa_risposta)
            if (f==True):
              ctrlIdont(domanda_fatta, stringa_risposta, "ing")
              return;
            ctrlIngredientsPotion(pozione_corrente, stringa_risposta)
            tentativi+=1;
        if (getCountFalse()==getDosi(pozione_corrente)):
            print(FrasiSimpleNlg.rispPitonNeg("ing"));
        if (getCountFalse()==0): 
            print( FrasiSimpleNlg.rispTuttiIng());
        elif (tentativi>=2): 
            print(FrasiSimpleNlg.rispIngMancanti());

#Funzione che controlla il dialogo nella situazione di domanda ingredienti  
def ControlloDomandaIngredienti(domanda_fatta, stringa_risposta):
    global ingrediente_scelto;
    global pozione_corrente;
    flag=ctrlValidPotion(stringa_risposta);
    f=frs(stringa_risposta);
    if(f==True):
      ctrlIdont(domanda_fatta, stringa_risposta, "poz")
      return;
    controllo=0;
    while (flag==False and controllo<2): 
        print(FrasiSimpleNlg.BackStrategy(1))
        stringa_risposta=input(domanda_fatta).lower()
        flag=ctrlValidPotion(stringa_risposta);
        controllo+=1;
    if (flag == False):
        print(FrasiSimpleNlg.BackStrategy(2));
        return
    f=frs(stringa_risposta);
    if(f==True): #risposta insicura
      ctrlIdont(domanda_fatta, stringa_risposta, "poz");
      return;
    #esce dal while se stringa_risposta contiene una pozione valida
    if (pozione_corrente in stringa_risposta): #risposta giusta
        frame_corrente[ingrediente_scelto]=True;
        print(FrasiSimpleNlg.rispPitonPos("poz"));
        tentativi=0;
        ctrlIngredientsPotion(pozione_corrente, stringa_risposta)
        while (getCountFalse()!=0 and tentativi<2): #frame non completo
            if (getCountFalse()==0):
                break;
            domanda_fatta=FrasiSimpleNlg.approfIng();
            stringa_risposta=input(domanda_fatta).lower();
            f=frs(stringa_risposta)
            if (f==True):
              ctrlIdont(domanda_fatta, stringa_risposta, "ing")
              return;
            ctrlIngredientsPotion(pozione_corrente, stringa_risposta)
            tentativi+=1;
        if (getCountFalse()==getDosi(pozione_corrente)):
            print(FrasiSimpleNlg.rispPitonNeg("ing"));
        if (getCountFalse()==0): 
            print( FrasiSimpleNlg.rispTuttiIng());
        elif (tentativi>=3): 
            print(FrasiSimpleNlg.rispIngMancanti());
    else: #l'utente non ha detto la pozione giusta
        print(FrasiSimpleNlg.rispPitonNeg("poz"));
        domanda_fatta= FrasiSimpleNlg.chiediIngPoz(pozione_corrente);
        stringa_risposta = input(domanda_fatta).lower();
        tentativi=0;
        ctrlIngredientsPotion(pozione_corrente, stringa_risposta)
        while (getCountFalse()!=0 and tentativi<2): 
            if (getCountFalse()==0):
                break;
            domanda_fatta=FrasiSimpleNlg.approfIng();
            stringa_risposta=input(domanda_fatta).lower();
            f=frs(stringa_risposta)
            if (f==True):
              ctrlIdont(domanda_fatta, stringa_risposta, "ing")
              return;
            ctrlIngredientsPotion(pozione_corrente, stringa_risposta)
            tentativi+=1;
        if (getCountFalse()==getDosi(pozione_corrente)):
            print(FrasiSimpleNlg.rispPitonNeg("ing"));
        if (getCountFalse()==0): 
            print( FrasiSimpleNlg.rispTuttiIng());
        elif (tentativi>=3): 
            print(FrasiSimpleNlg.rispIngMancanti());
            
#Funzione che controlla il dialogo nella situazione di domanda pozione  
def ControlloDomandaPozione(domanda_fatta, stringa_risposta):
    flag=ctrlValidIngr(stringa_risposta);
    f=frs(stringa_risposta);
    if(f==True):
      ctrlIdont(domanda_fatta, stringa_risposta, "ing")
      return;
    controllo=0; 
    while (flag==False and controllo<2):
        print(FrasiSimpleNlg.BackStrategy(1))
        stringa_risposta=input(domanda_fatta).lower()
        flag=ctrlValidIngr(stringa_risposta);
        controllo+=1;
    if (flag==False):
        print(FrasiSimpleNlg.BackStrategy(2))
        return
    #è uscito dal while quindi stringa_risposta ha un ingrediente valido
    tentativi=0;
    f=frs(stringa_risposta)
    if (f==True):
      ctrlIdont(domanda_fatta, stringa_risposta, "ing")
      return;
    ctrlIngredientsPotion(pozione_corrente, stringa_risposta)
    while (getCountFalse()!=0 and tentativi<2): #frame incompleto e tentativi finiti
        if (getCountFalse()==0):
            break;
        domanda_fatta=FrasiSimpleNlg.approfIng();
        stringa_risposta=input(domanda_fatta).lower();
        f=frs(stringa_risposta)
        if (f==True):
          ctrlIdont(domanda_fatta, stringa_risposta, "ing")
          return;
        ctrlIngredientsPotion(pozione_corrente, stringa_risposta)
        tentativi+=1;
    if (getCountFalse()==getDosi(pozione_corrente)):
        print(FrasiSimpleNlg.rispPitonNeg("ing"));
    if (getCountFalse()==0): 
        print( FrasiSimpleNlg.rispTuttiIng());
    elif (tentativi>=3): 
        print(FrasiSimpleNlg.rispIngMancanti());

#Funzione che controlla le risposte. Il DM smista le funzioni che effettuano il controllo in base alla domamda che è stata proposta
def getKeyAnswer():
    global pozione_corrente
    global ingrediente_scelto
    global stringa_risposta
    global tag;
    global domanda_fatta
    if(tag == "domanda_ingrediente"):
      ControlloDomandaIngredienti(domanda_fatta, stringa_risposta)
    if(tag == "domanda_trabocchetto"):
      controlloDomandaTrabocchetto(domanda_fatta, stringa_risposta)
    if(tag == "domanda_pozione"):
      ControlloDomandaPozione(domanda_fatta, stringa_risposta);

#2)Parte della Memoria 
#Si creano due frame, una ingredienti nominati e l'altra degli ingredienti ignorati e l'indice riga corrisponde alla pozione
def store():  #indice 0 = antidote to common poisons
              #indice 1 = distillation of living death
              #indice 2 = pompio potion
  global currentIndex
  IgredientiNominati={};
  IgredientiIgnorati={};
  IgredientiNominati.setdefault(str(currentIndex),getKeyValueTrue()); #il frame della memoria estrapola informazioni
  #dal frame corrente utilizzando le funzioni getKeyValueTrue() e getKeyValueFalse()
  IgredientiIgnorati.setdefault(str(currentIndex),getKeyValueFalse());
  return IgredientiNominati, IgredientiIgnorati;

#Funzione che estrapola le informazioni dalla memoria (store())
def findDataStore(numero_pozione, tipo_dato): #da richiamare quando tutte e tre le pozioni sono state interrogate.
  ingredientiNominati, ingredientiIgnorati=store();
  if (tipo_dato == "Detti"):
    for chiave, valore in ingredientiNominati.items():
      if (chiave== str(numero_pozione)):
        return len(valore)
  if (tipo_dato == "Non Detti"):
    for chiave, valore in ingredientiIgnorati.items():
      if (chiave== str(numero_pozione)):
        return len(valore)

#Funzioni per il calcolo del voto finale (parte del Voto)
def CalcoloPunteggi(numero_pozione, voto_massimo, lung_ing_detti):
    lung_tot_ing = getDosi(nomi_pozioni[numero_pozione])
    punti=round((voto_massimo * lung_ing_detti)/lung_tot_ing, 0)
    return punti

#Funzione che assegna il voto. Ogni pozione scelta vale dei punti in corrispondenza alla difficoltà della stessa.   
def AssegnaVoto():
    voto_massimo = 0
    punteggio = []
    voto_finale = 0
    #Creiamo variabile che prende il punteggio di ciascuna pozione (che ci serve per il voto), considerando che il massimo del punteggio deve fare 30. 
    frame_punteggi = {
        nomi_pozioni[0]: 10,
        nomi_pozioni[1]: 15,
        nomi_pozioni[2]: 5
            }
    punti = CalcoloPunteggi(currentIndex, frame_punteggi[nomi_pozioni[currentIndex]], findDataStore(currentIndex, "Detti"))
    punteggio.append(punti)
    for j in range(len(punteggio)):
        voto_finale += punteggio[j]
    return punteggio, voto_finale
#AssegnaVoto()

def main():
    global frame_corrente
    global ing
    global indici
    m = [0,1,2] 
    n = random.choice(m)
    punteggio=[];
    valutazione=0;
    array = FrasiSimpleNlg.FraseIniziale(n) #Il sistema di dialogo prende l'iniziativa generando il linguaggio con la librearia simpleNLG
    for i in range (len(array)-1):
        print(array[i])
        time.sleep(1.5)
    name = input(array[i+1])
    array = FrasiSimpleNlg.fraseIntro(name)
    for i in range(len(array)):
        print(array[i])
        time.sleep(1.5)
    while(len(indici) != 0):
        frame_corrente = createFrame() 
        ing = list(frame_corrente.keys())
        queries()
        getKeyAnswer()
        time.sleep(2.5)
        punti, voto_finale= AssegnaVoto();
        punteggio.append(punti);
        valutazione+=voto_finale;
        frame_corrente.clear()
    print (punteggio, valutazione)
    FrasiSimpleNlg.commentoVoto(valutazione); #in base alla votazione, si generano delle risposte diverse con cui Piton valuta lo studente
main()
