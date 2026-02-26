import math
from math import sqrt
from math import factorial as fact
import random
from datetime import datetime, date, time, timedelta
import locale
#   nome = "Marco"
#   eta = 25
#   print(nome)
#   print(eta)
#   print("Ciao")

#   x = 42
#   print(type(x))
""" y = " ciao"
    print(type(y))

    a = 10
    b = 3
    print(a + b)
    print(a//b)
    print(a **b)"""
""" s1 = "Leader "
    s2 = "Formazione "
    print(s1 + " " + s2)
    print(s1 * 3)
    a, b, c = 10, 20 ,30
    nome1, nome2, nome3 = "marco", "michele", "maurizio"
    print(nome3)
    print (a)"""
#   eta = 40
#   anno = 1985
#   nome = "Anna"
#   print(nome + "e' nata nel " + anno) #errato
#   print(nome + " e' nata nel " + str(anno)) #giusto metodo 1 per poche variabili 
#   print(f"{nome} e' nata nel {anno}") #metodo + giusto con tante variabili 

""" x = 10

    def mia_funzione():
        y = 5
        print("Dentro la funzione:", y)

    mia_funzione()
    print("Fuori dalla funzione:", x)

    nome = input(" PROF SCRIVA QUI FORZA MILAN ")
    print(" FORZA MILAN "+" FORZA MILAN! "+ " FORZA MILAN "  " FORZA MILAN "+" FORZA MILAN! "+ " FORZA MILAN " + nome + "!")"""

""" eta = int(input("Inserisci la tua età: "))
    print(f"L'anno prossimo avrai {eta + 1} anni.")"""

#   ESERCIZIO1 1.Assegna il tuo nome a una variabile. 2. Chiedi il tuo nome utente 3.Stampa a schermo <<Piacere di conoscerti>>

#   nome1 = "Marco"
#   nome2 = input("Come ti chiami? ")
#   print(f" Ciao {nome2} mi chiamo :  {nome1}")

#   nome3 =  "MILAN"
#   nome4 = input("prova a chiedere chi vince il campionato ")
#   print(f" {nome4},ovvio vince  la squadra : {nome3} ")

#   ESERCIZIO2 1. chiedi due numeri all'utente 2.Scrivi la somma è e inserisci la somma dei due numeri 3.Fai anche la sottreazione,la moltiplicazione  e la divisione, allo stesso modo

#   nome5 = int(input("inserisci il primo numero: "))
#   nome6 = int(input("inserisci il secondo numero: "))
#   print(f"{nome5 + nome6}")
#   print(f"{nome5 / nome6}")
#   print(f"{nome5 * nome6}")
#   print(f"{nome5 - nome6}")

#   frutta = ["Mela", "Banana", "Arancia", "kiwi", "Pera"]
#   for frutto in frutta:
#       print(frutto)
#   print(frutta[-1])
#   print(frutta[-2])
#
#   print(frutta[0:5]) #dal primo all quinto elemento
#   print(frutta[:3]) #fino al terzo elemento
#   print(frutta[2:]) #parte dal secondo elemento
#   print(frutta[-3:]) #vai indietro di tre partendo dall ultimo elemento

#   cambiare un elemento
#   numeri = [10, 20, 30, 40]
#   numeri[1] = 25  #cambia la posizione dell elemento nell array alla posizione 1 cioe 20
#   print(numeri)

#   aggiungere un elemento alla fine append()
#   frutta = ["Mela", "Banana", "Arancia", "kiwi", "Pera"]
#   frutta.append("Mango")
#   print(frutta)

#   inserisce elemento in una posizione specifica
#   frutta = ["Mela", "Banana", "Arancia", "kiwi", "Pera"]
#   frutta.insert(2,"Fragola")
#   print(frutta)

#   rimuovere un elemento
#   frutta = ["Mela", "Banana", "Arancia", "kiwi", "Pera"]
#   frutta.remove("Mela")
#   print(frutta)

#   rimuovere l ultimo elemento
#   frutta.pop()

#   rimuovere con l'indice dell elemento
#   del frutta[1]

#   rimuovere tutto
#   frutta.clear()

#   Mettere in ordine
#   frutta.sort()

#   Mettere ordine al contrario
#   frutta.sort(reverse=True)

#   Invertire la lista
#   frutta = ["Mela", "Banana", "Pera", "Kiwi"]
#   frutta.reverse()
#   print(frutta)


#   Verificare se un elemento è presente in
#   frutta = ["Mela", "Pera"]
#   if "Mela" in frutta:
#       print("Mela è nella lista!")

#   frutta = ["Mela", "Banana", "Pera", "Kiwi"]
#   for frutto in frutta:
#       print(frutto)

#   Scorrere per ottenere indice + valore
#   frutta = ["Mela", "Banana", "Pera", "Kiwi"]
#   for i, frutto in enumerate(frutta):
#       print(f"{i}: {frutto}")

#   frutta = ["Mela", "Banana", "Pera", "Kiwi"]
#   frutta.reverse()
#   print(frutta)

#   Chiediamo i dati all'utente
#   eta = int(input("Inserisci la tua età: "))
#   patente_input = input("Hai la patente? (si/no): ")

#   Convertiamo la risposta in booleano
#   if patente_input == "si":
#       patente = True
#   else:
#       patente = False

#   DEBUG: stampiamo i valori
#   print("DEBUG ----------------")
#   print(f"Età: {eta}")
#   print(f"Patente (boolean): {patente}")
#   print("----------------------")

#   Controllo con operatore AND
#   if eta >= 18 and patente:
#       print("Puoi guidare 🚗")
#   else:
#       print("Non puoi guidare ❌")

#   print(eta >= 18)

# ESERCIZIO: chiedere all utente che squadra il nome,la squadra preferita,numero di gol segnati dalla squadra, numero di gol subiti dalla squadra

#nome = input("Inserisci il tuo nome : ")
#squadra_preferita = input("Squadra preferita? ")
#gol_segnati = int(input("Gol segnati dalla squadra: "))
#gol_subiti = int(input("Gol subiti dalla squadra: "))

#if squadra_preferita == "Roma":
#    print("Consiglio di cambiare squadra")
#else:
#    if gol_segnati > gol_subiti and gol_segnati >= 2:
#        print(f"Ciao {nome}, la tua squadra ha vinto con almeno 2gol!")
#    elif gol_segnati == gol_subiti or gol_segnati == 0:
#        print(f"Ciao {nome}, la squadra ha pareggiato") 
#    else:
#        print(f"Ciao {nome}, la tua squadra ha perso")  

#   //Scorrere i primi elementi di una lista con slicing
#   frutta = ["Mela", "Banana", "Arancia", "Kiwi"]
#   for frutto in frutta[:3]:
#        print(frutto)

#   Scorrere i primi elementi di una lista con range()
#   frutta = ["Mela", "Banana", "Arancia", "Kiwi","Pera"]
#   for i in range(3):
#    print(frutta[i])

#   Scorrere i primi elementi di una lista con enumerate()

#   frutta = ["Mela", "Banana", "Arancia", "Kiwi","Pera"]
#   for i, frutto in enumerate(frutta):
#        if i < 3:
#            print(f"Frutto {i}: {frutto}")

#   Copiare una lista che non crea un duplicato costante di una lista

#   lista1 = [1, 2, 3]          
#   lista2 = lista1.copy()      cosi da poter modificare lista2 e non toccare la lista1
#   lista2.append(4)
#   print(lista1)

#   Metodo sconsigliato, perche lista2 rimanda alla stessa lissta1 e quindi una modifica a lista2 modifica nache lista1
#   NON SI FA MAI

#   lista1 = [1, 2, 3]
#   lista2 = lista1
#   lista2.append(4)
#   print(lista1)

#   DIZIONARIO 
#   studente = {
#    "nome": "Mario",
#    "età": 30,
#    "modulo": "UFC12 - Python"
#}
#print(studente)
#print(studente["nome"])
#print(studente["età"])
#print(studente["modulo"])

#   Accedere ai valori del dizionario se la chiave non esiste METODO CORRETTO
#   print(studente.get("cognome", "Non disponibile"))

#   Aggiungere un nuovo elemento (chiave e valore) al dizionario

#   studente["sede"] = "Leader" 
#   print(studente)

#   Modificare un elemento
#   studente["età"] = 10
#   print(studente)

#   Eliminare un elemento dal dizionario

#   del studente["nome"]
#   print(studente)

#   Rimuovere un elemento con .pop() mantenere comunque in memoria e ottenere il valore massimo

#   eta_rimossa = studente.pop("età")
#   print(f"questa è l'età rimossa {eta_rimossa}")
#   print(studente)

#   Eliminare tutto il dizionario

#   studente.clear()

#   Vedere ogni chiave di un dizionario

#   for chiave in studente:
#       print(chiave)

#   Vedere ogni valore di un dizionario

#   for valore in studente.values():
#    print(valore)

#   Scorrere chiavi e valori del dizionario

#   for chiave, valore in studente.items():
#   print(f"{chiave}: {valore}")

#   Fare un check se esiste una chiave

#   if "nome" in studente:
#       print("La chiave 'nome' è presente!")
#   if "diploma" not in studente:
#       print("Diploma aggiunto con successo")

#   Verificare se un valore esiste con .values()

#   if "Mario" in studente.values():
#       print("il valore 'Mario' è presente!")

#   ricerca = input("inserisci nome: ")
#   if ricerca in studente.values():
#       print("il valore sta a ")

#           DIZIONARI ANNIDATI


#   studenti = {
#       "studente1": {
#           "nome": "Mario",
#           "età": 20,
#           "modulo": "Python"
#       },
#       "studente2": {
#           "nome": "Anna",
#           "età": 22,
#           "modulo": "Linuc server"
#       },
    
#   }

#   Accedere a un valore specifico

#   print(studenti["studente1"] ["nome"])



#   studenti["studente3"] = studenti
#   print(studenti)

#   Modificare l'età o altro

#   studenti["studente1"]["età"] = 21
#   print(studenti)

#   ITERAZIONE CICLO FOR IN UN DIZIONARIO ANNIDATO

#   for chiave_studente, dati in studenti.items():
#       print(("-")*20)
#       print(f"ID: {chiave_studente}")
#       for chiave, valore in dati.items():
#           print(f"    {chiave}: {valore}")

#   Eliminare una chiave specifica nel dizionare annidato

#   del studenti["studente1"]["età"]

#   Eliminare completamente un elemento

#   del studenti["studente2g"]

#   Elif permette di inserire piu condizioni

#   eta = int(input"Inserisci la tua età:"))

#   if eta < 18:
#       print("Sei minorenne.")
#   elif eta >= 18 and eta <65:
#       print("Sei un adulto.")
#   else:
#       print("Sei un anziano.")

#   Creare un if else in una sola riga

#   status = "Maggiorenne" if eta >= 18 else "Minorenne"
#   print(status)

#      CICLO WHILE

#   x = 0
#   while x < 10:
#       if x ==5:
#           break
#       print(x)
#       x += 1

#   ciclo che salta il x = 3

#   x = 0
#   while x < 5:
#       x+= 1
#       if x == 3:
#           continue
#       print(x) 

#       TRY-EXCEPT

#   while True:
#       try:
#           numero = int(input("Inserisci un numero: "))
#           print(f"Hai inserito: {numero}")
#           break
#       except ValueError:
#           print("Errore: Devi inserire un numero valido! Riprova.")

#       TRY EXCEPT IN UN CICLO FOR

#   numeri = ["10", "5", "quattro", "8", "zero", "15"]

#   for num in numeri:
#   try:
#           risultato = int(num) * 2
#           print(f"Doppio di {num}: {risultato}")
#       except ValueError:
#           print(f"Errore: '{num}' non è un numero valido")

#   stipendi = ["1500", "tremila", "1200", "399"]

#   for stip in stipendi:
#       try:
#           stipendio= int(stip) / 2
#           print(f"il risultato è {stipendio}")
#       except ValueError:
#           print(f"non è stato possibile: '{stip}' ")

#   Creiamo un ciclo infinito

#   while True:
#       risposta = input("Scrivi 'stop' per uscire ")
#       if risposta == "stop":
#           print("Ciclo interrotto.")
#           break

#   Validiamo l input di un utente con try except

#   while True:
#       try:
#           numero = int(input("Inserisci un numero positivo: "))
#           if numero > 0:
#               print(f"Hai inserito {numero}, valido!")
#               break
#           else:
#               print("Errore: Il numero deve essere positivo.")
#       except ValueError:
#           print("Errore: Devi inserire un numero!")

#   Saltare un iterazione senza interrompere il ciclo

#   while True:
#       try:
#           numero = int(input("Inserisci un numero (0 per uscire): "))
#           if numero == 0:
#               print("Ciclo terminato.")
#               break # Esce dal ciclo

#           if numero < 0:
#               print("Numeri negativi non ammessi, riprova")
#               continue

#           print(f"Hai inserito il numero {numero}")

#       except ValueError:
#           print("Un numero non altro, grazie ")

#   print(math.pi)
#   dir(math)

#   print(sqrt(16))
#   print(dir(math))

#   import math as m
#   print(m.sqrt(16))

#   print(fact(5))

#   NUMERI RANDOM

#   import random
#   print(random.random())

# numero da 1 a 100 0gni 5

#   import random
#   print(random.randrange(0,100,5))

#   Numero da random da 1 a 10
#   import random
#   print(random.int(1,10))

#   Numero random

#   print(random.uniform(10,50))

#   frutti = ["Mela", "Banana", "Uva", "Arancia"]
#   scelta = random.choice(frutti)
#   print("Frutto scelto:", scelta)

#   Random di ogni frutto puo uscire uno di questi
#   frutti = ["Mela", "Banana", "Uva", "Arancia"]
#   scelta = random.choices(frutti,k=4)
#   print("Frutto scelto:", scelta)

#       random non ti esce piu un duplicato

#   frutti = ["Mela", "Banana", "Uva", "Arancia"]
#   scelta = random.sample(frutti, k = 4)
#   print("Frutto scelto:", scelta)

#   for frutto in frutti:
#    print(f"{frutto}")

#       Mischiare il tutto

#   frutti = ["Mela", "Banana", "Uva", "Arancia"]
#   random.shuffle(frutti)
#   print("frutto scelto è: ", frutti)

#       DATE TIME

#   ora_corrente = datetime.now()
#   print("Ora attuale: ", ora_corrente)

#   ora_corrente = datetime.now()
#   print("Ora attuale:", ora_corrente)
#   data_formattata = ora_corrente.strftime("%d/%m/%Y - %H:%M:%S")
#   print("Data formattata:", data_formattata)

#   oggi = date.today()
#   ora_corrente = datetime.now()
#   orario_personalizzato = time(23, 59, 59)

#   print("Data di oggi: ", oggi)
#   print("Ora attuale:", ora_corrente)
#   print("Orario personalizzato: ", orario_personalizzato)

#   Quanti giorni mancano al compleanno

#   oggi = date.today()
#   evento = date(2026, 8, 19)  
#   differenza = evento - oggi
#   print(f"Mancano {differenza.days} giorni alla fine dell'anno!") #il days sta nel metodo dell import date

#   CONVERTIRE UNA DATA
#   data_str = "10/04/2024 14:30"
#   data_convertita = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
#   print("Data convertita: ", data_convertita)

#   ESERCIZIO: prendere 2 date e contare quanti giorni mancano per arrivare da data 1 a data2

#data1_str = input("Inserisci il giorno,mese e anno della prima data (gg/mm/aaaa): ")
#data2_str = input("Inserisci ora e minuti (hh:mm): ")
#data3_str = input("Inserisci il secondo giorno,mese e anno (gg/mm/aaaa): ")
#data4_str = input("Inserisci l' ora e minuti: ")

#data2 = datetime.strptime(data1_str, "%d/%m/%Y")
#data3 = datetime.strptime(data2_str, "%H:%M")
#data4 = datetime.strptime(data3_str, "%d/%m/%Y")
#data5 = datetime.strptime(data4_str,"%H:%M")
#differenza_giorni = data2 - data4
#differenza_minuti = data3 - data5
#giorni = differenza_giorni.days
#differenza_minuti = differenza_giorni.seconds
#print(f"Differenza giorni: {differenza_giorni}, differenza minuti {differenza_minuti} - ")

#data1 = datetime.strptime(data1_str, "%d/%m/%Y %H:%M")
#data2 = datetime.strptime(data2_str, "%d/%m/%Y %H:%M")

#differenza = data1 - data2
#giorni = differenza.days
#minuti = differenza.seconds
#smin = int(minuti)/60

#print(f"Differenza: {differenza} - {giorni} - {smin}")



#   CONVERTIRE UNA DATA IN FORMATO DATA ITALIANO

#   data = datetime(2026, 2, 15, 16, 42)
#   data_str = data.strftime("%d/%m/%Y %H:%M")
#   print("Data formattata:", data_str)

#   Creare una data personalizzata

#   compleanno = datetime(1990, 5, 15, 8, 30)
#   print("Il compleanno impostato è:", compleanno.strftime("%A %d %B %Y, %H:%M"))

#   AGGIUNGERE O SOTTRARRE GIORNI DA UNA DATA CON GIORNI ITALIANIì

#oggi = datetime.now()
#prossima_Settimana = oggi + timedelta(days=7) #Aggiunge 7 giorni
#ieri = oggi - timedelta(days=1) #Sottrae 1 giorno

#locale.setlocale(locale.LC_TIME, "italian")

#print("Oggi:", oggi.strftime("%A %d/%m/%Y"))
#print("Tra 7 giorni:", prossima_Settimana.strftime("%d/%m/%Y"))
#print("Ieri:", ieri.strftime("%d/%m/%Y"))

#       SCRIVERE  UNA DATA PERSONALIZZATA IN ITALIANO

#   locale.setlocale(locale.LC_TIME, "it_IT.UFT-8")
#   locale.setlocale(locale.LC_TIME, "it_IT")
#   locale.setlocale(locale.LC_TIME, "italian")
#   data = datetime(2024, 4, 10, 14, 30)
#   data_str = data.strftime("%A %d %B %Y, ore %H:%M")
#   print("Data in italiano:", data_str)
