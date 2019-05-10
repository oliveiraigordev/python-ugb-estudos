from Elemento import Elemento
class NoABB:
	def __init__ (self):
		self._fe = None
		self._fd = None
		self._elemento = Elemento()
	def getFe(self):
		return self._fe
	def setFe(self,n):
		self._fe = n
	def getFd(self):
		return self._fd
	def setFd(self,n):
		self._fd = n
	def getElemento(self):
		return self._elemento
	def setElemento(self,n):
		self._elemento = n