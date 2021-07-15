import pdb


lista = [[2, 4, 1], [ 1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]
print(lista)

pdb.set_trace()
lista2 = [max(i) for i in lista]
print(lista2)