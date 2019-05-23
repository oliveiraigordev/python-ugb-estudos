from request import Codenation

main_app = Codenation()
print(main_app.requestGet('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=86de2aa6467af87f566c7c4bb33b75f7e8ce84ad'))

#metodo contem string default = '' para rodar fazer primeiramente a requisicao do JSON  
print('\nSHA1:')
print(main_app.criptografia('the internet? is that thing still around? homer simpson'))

