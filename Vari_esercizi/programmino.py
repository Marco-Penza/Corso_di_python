# STEP 1  gioco base in cui il computer genera un numero casuale e ò'utente deve indovinarlo senza limiti di tentativi.

import random
import json
from datetime import datetime


def carica_risultati(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def salva_risultato(file, risultato) :
    risultati = carica_risultati(file)
    risultati.append(risultato)
    with open(file, 'w') as f:
        json.dump(risultati, f, indent=4)

def mostra_classifica(file):
    risultati = carica_risultati(file)
    if not risultati:
        print("Nessun risultato disponibile.")
        return
    print("\nClassifica:")
    risultati_ordinati = sorted(risultati, key=lambda x: (x['risultato'] != "Vittoria",x['tentativi']))
    for i, r in enumerate(risultati_ordinati, start=1):
        print(f"{i}. {r['nome']} - Tentativi: {r['tentativi']} - Data: {r['data']} - Risultato: {r['risultato']}")


nome_giocatore = input("Inserisci il tuo nome: ")
file_risultati = "file_risultati.json"
numero_min = int(input("Qual'è il numero minimo da indovinare? "))
numero_max = int(input("Qual'è il numero massimo da indovinare? "))
max_tentativi = int(input("Quanti tentativi vuoi avere per indovinare il numero? "))
numero_segreto = random.randint(numero_min, numero_max)
tentativi = 0
print(numero_segreto)
print(f"Sto pensando a un numero tra {numero_min} e {numero_max}. Hai {max_tentativi} tentativi per indovinarlo!")
risultato_finale = "Sconfitta"
while tentativi < max_tentativi:
    try:
        tentativo = int(input(f"Tentativo {tentativi + 1}/{max_tentativi}: Inserisci un numero: "))
        if tentativo < numero_min or tentativo > numero_max:
            print(f"Il numero deve essere tra {numero_min} e {numero_max}")
        else:
            tentativi +=1
       
            if tentativo < numero_segreto:
                print("Troppo basso!")
            elif tentativo > numero_segreto:
                print("Troppo alto!")
            else:
                print(f"Hai indovinato, il numero era {tentativo} in {tentativi} tentativi!")
                risultato_finale = "Vittoria"
                break
        
        

    except ValueError:
        print("Inserire solo il numero")

if tentativi == max_tentativi and tentativo != numero_segreto:
    print(f"Mi dispiace, hai esaurito i tentativi! Il numero segreto era {numero_segreto}.")

risultato = {
    "nome": nome_giocatore,
    "data": datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
    "tentativi": tentativi,
    "risultato": risultato_finale
}

salva_risultato(file_risultati, risultato)
mostra_classifica(file_risultati)