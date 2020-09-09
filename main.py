from Lista import Lista

list = Lista()
list.adicionar(15)
list.adicionar(5)
list.adicionar(10)
list.adicionar(20)
list.adicionar(55)
print("Tamanho da lista: " + str(list.tamanho))
list.printListOrdered()
list.printReverseOrder()

value = input("Digite um valor: ")
list.adicionar(value)
list.printListOrdered()
list.printReverseOrder()