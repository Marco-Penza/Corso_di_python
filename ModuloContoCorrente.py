from datetime import datetime
import json

class ContoCorrente:

    def __init__(self, nome, saldoIniziale = 0, fileTransazioni = "transazioni.json")
        self.nome = nome.lower()
        self.__saldo = saldoIniziale
        self.transazioni = []
        self.fileTransazioni = fileTransazioni
        self.caricaTransazioni()
        self.registraTransazione("Apertura conto", saldoIniziale)

    def deposita(self, importo):
        if importo > 0:
            self.saldo += importo
            self.registraTransazione("Deposito", importo)
            print(f"Hai depositato {importo}€. Saldo attuale: {self.__saldo}€ ")
        else:
            print("L' importo del deposito deve essere positivo. ")

    def preleva(self, importo):
        if 0 < importo <= self.__saldo:
            self.__saldo -= importo
            self.registraTransazione("Prelievo", - importo)
            print(f"Hai prelevato {importo}€. Saldo attuale: {self.__saldo}€ ")
        elif importo > self.__saldo:
            print("Saldo insufficiente per il prelievo." )
        else:
            print("L'importo del prelievo deve essere positivo ")

    def getSaldo(self):
        return self.__saldo
    
    def registraTransazione(self, tipo, importo):
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transazione = {"data": data, "tipo": tipo, "importo": importo}
        self.transazioni.append(transazione)
        self.salvaTransazioni()

    def mostraCronologia(self):
        if not self.transazioni:
            print("Non ci sono transazioni disponibili.")
        else:
            print("\nCronologia delle transazioni:")
            for t in self.transazioni:
                print(f"{t['data']} - {t['tipo']}: {t['importo']}€")