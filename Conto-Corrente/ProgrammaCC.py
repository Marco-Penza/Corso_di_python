from ModuloContoCorrente import ContoCorrente

nomeUtente = input("Inserisci il tuo nome: ")
conto = ContoCorrente(nomeUtente, 0)

# Menu Interattivo
while True:
    print("\n--- Menu ---")
    print("1. Deposita denaro")
    print("2. Preleva denaro")
    print("3. Visualizza saldo")
    print("4. Mostra cronologia delle transazioni")
    print("5. Esci")

    scelta = input("Scegli un'opzione (1-5): ")
    if scelta == "1":
        try:
            importo = float(input("Inserisci l'importo da depositare: "))
            conto.deposita(importo)
        except ValueError:
            print("Errore: Inserisci un numero valido.")
    elif scelta == "2":
        try:
            importo = float(input("Inserisci l'importo da prelevare: "))
            conto.preleva(importo)
        except ValueError:
            print("Errore: Inserisci un numero valido. ")
    elif scelta == "3":
        print(f"Il tuo saldo corrente è: {conto.getSaldo()}€")
    elif scelta == "4":
        conto.mostraCronologia()
    elif scelta == "5":
        print("Grazie per aver usato il nostro sistema. Arrivederci!")
        break
    else:
        print("Scelta non valida. Riprova.")