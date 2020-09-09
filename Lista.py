from No import No

class Lista:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def adicionar(self, value):
        if self.primeiro:
            aux = self.primeiro
            anterior = None
            while(aux.proximo):
                anterior = aux
                aux = aux.proximo
            aux.proximo = No(value)
            aux.proximo.anterior = aux
            aux.anterior = anterior
            if self.ultimo:
                self.ultimo = aux.proximo
        else:
            self.primeiro = No(value)
            self.ultimo = No(value)
        self.tamanho += 1


    def printListOrdered(self):
        if self.primeiro == None:

            aux = self.primeiro
            while(aux):
                print(aux.report)
                aux = aux.proximo

    def printReverseOrder(self):
        aux = self.ultimo
        print("Tamanho da lista em ordem reversa: " + str(self.tamanho))
        while(aux):
            print(aux.report)
            aux = aux.anterior
        print("\n FIM DA LISTA \n")