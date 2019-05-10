from Elemento import Elemento
from NoABB import NoABB
from ABB import ABB

a=ABB()
a.insereNo(8)
a.insereNo(12)
a.insereNo(4)
a.insereNo(14)
a.insereNo(2)
a.insereNo(6)
a.insereNo(10)
a.insereNo(7)
a.insereNo(9)
a.insereNo(5)
a.insereNo(3)
a.insereNo(11)
a.insereNo(13)
a.insereNo(15)
a.insereNo(1)
'''
a.preOrdem(a.getRaiz())
print('-'*20)
a.emOrdem(a.getRaiz())'''
print(a.contaElementos(a.getRaiz()))
if a.procuraElemento(a.getRaiz(),a.getRaiz(),8):
	print('Elemento está na árvore')
	