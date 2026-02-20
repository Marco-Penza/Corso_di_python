"""class Studente:
    def __init__(self, nome, eta, codice_studente):
        self.nome = nome
        self.eta = eta
        #self.codice.studente = codice_studente     Versione Pubblica
        self.__codice_studente = None           #Versione privata
        self.set_codice_studente(codice_studente)

    def descrizione(self):
        return f"{self.nome} ha {self.eta} anni. {self.get_codice_studente} "
    
    def get_codice_studente(self):
        return self.__codice_studente
    
    def set_codice_studente(self, nuovo_codice):
        if nuovo_codice.startswith("S") and len(nuovo_codice) == 8:
            self.__codice_studente = nuovo_codice
        else:
            print("Errore: Il codice deve iniziare con 'S' e avere 8 caratteri ")


studente1 = Studente("Anna",20, "S1234567")
print(studente1.get_codice_studente())
"""

class Studente:
    def __init__(self, nome, eta, codStud):
        self.nome = nome
        self.eta = eta
        self.codStud = codStud
        
        

    def descrizione(self):
        desk1 = f"Nome: {self.nome}, Età: {self.eta}, Codice: {self.codStud} {self.extra()}"
        if hasattr(self, "corsoDiLaurea"):
            desk1 += f"Corso: {self.corsoDiLaurea}"
        elif hasattr(self, "indirizzo"):
            desk1 += f"Indirizzo: {self.indirizzo}"
        return desk1

    def tipoStudente(self):
        return "Studente generico"

    def extra(self):
        return ""
    
class StudenteUniversitario(Studente):
    def __init__(self, nome, eta, codStud, corsoDiLaurea):
        super().__init__(nome, eta, codStud)
        self.corsoDiLaurea = corsoDiLaurea
    
    def tipoStudente(self):
        return "Studente Universitario"

    def extra(self):
        return f"Corso di laurea : {self.corsoDiLaurea}"
    
class StudenteLiceale(Studente):
    def __init__(self, nome, eta, codStud, indirizzo):
        super().__init__(nome, eta, codStud)
        self.indirizzo = indirizzo
    
    def tipoStudente(self):
        return "Studente Liceale"
    
    def extra(self):
        return f"Studente Liceale : {self.indirizzo}"
    
#Creazione degli oggetti

studenteGenerico = Studente("Marco", 18, "S1234567")
studenteUni = StudenteUniversitario("Anna", 21, "S7654321", "Ingegneria Informatica")
studenteLiceale = StudenteLiceale("Giulia", 16, "S4567890", "Scientifico")

studenti = [studenteGenerico, studenteUni, studenteLiceale]

for studente in studenti:
    print(studente.descrizione())
    print(f"Tipo di studente: {studente.tipoStudente()}\n")