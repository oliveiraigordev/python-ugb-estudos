from Elemento import Elemento
from NoABB import NoABB
class ABB:
	def __init__ (self):
		self._raiz = None
	def getRaiz(self):
		return self._raiz
	def setRaiz(self,n):
		self._raiz = n
	def arvoreVazia(self):
		return self._raiz == None
	def criaNo(self,n):
		no = NoABB()
		no.getElemento().setChave(n)
		return no
	def insereNo(self,n):
		if self.arvoreVazia():
			self.setRaiz(self.criaNo(n))
		else:
			self.insere(None,self.getRaiz(),n)
	def insere(self,pai,atual,n):
		if atual != None:
			if n < atual.getElemento().getChave():
				self.insere(atual,atual.getFe(),n)
			else:
				self.insere(atual,atual.getFd(),n)
		else:
			x = self.criaNo(n)
			if n < pai.getElemento().getChave():
				pai.setFe(x)
			else:
				pai.setFd(x)
	def preOrdem(self,no):#raiz
		if no != None:
			self.preOrdem(no.getFe())
			self.preOrdem(no.getFd())
			print(no.getElemento().getChave())
	def emOrdem(self,no):
		if no != None:
			self.emOrdem(no.getFe())
			print(no.getElemento().getChave())
			self.emOrdem(no.getFd())
	def remove(self,n):
		if not self.arvoreVazia():
			x = self.getRaiz()
			if n == x.getElemento().getChave(): #raiz é o unico nó da arvore
				if x.getFe() == None and x.getFd() == None:
					self.setRaiz(None)
				elif x.getFe() != None and x.getFd() == None: #somente 1 filho
					self.setRaiz(x.getFe())
					x.setFe(None)
				elif x.getFe() == None and x.getFd != None:
					set.setRaiz(x.getFd())
					x.setFd(None)
				else: #2 filhos
					self.removeNT(x,x,getFe())
	def procuraElemento(self,pai,atual,n):
		if atual != None:
			if n < atual.getElemento().getChave():
				self.procuraElemento(atual,atual.getFe(),n)
			elif n > atual.getElemento().getChave():
				self.procuraElemento(atual,atual.getFd(),n)
			elif n == atual.getElemento().getChave():
				return True
		else:
			return False
		
	def contaElementos(self,atual):
		if not self.arvoreVazia():
			cont = 1
			if atual.getFe() != None:
				cont = cont + self.contaElementos(atual.getFe())
			if atual.getFd() !=None:
				cont = cont + self.contaElementos(atual.getFd())
			return cont
	def contaElementos2(self,n):
		if n != None:
			x = contaElementos2(n.getFe())
			y = contaElementos2(n.getFd())
			return x + y + 1
		return 0

