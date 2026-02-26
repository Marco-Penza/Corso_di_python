class Studente:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età
    
studente1 = Studente("Anna", 20)
print(studente1.nome)
print(studente1.età)