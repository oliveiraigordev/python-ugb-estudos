import requests
import hashlib

class Codenation():
    def requestGet(self, url):
        resposta = requests.get(url)
        get_json = resposta.text
        with open ('answer.json','w') as arq:
            arq.write(get_json)
        return 'Arquivo JSON foi gerado'
    def criptografia(self, texto=''):
        decifrado = texto
        result = hashlib.sha1(decifrado.encode())
        return result.hexdigest()


