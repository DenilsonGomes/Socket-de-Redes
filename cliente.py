print 'Autores: Denilson Gomes Vaz da Silva e Julio Cesar Rodrigues'
print 'Trabalho de Redes'
print 'Implementação de Sockets\n'
#importação de modulos
import socket

host = socket.gethostbyname(socket.gethostname()) #atribui seu endereço IP a variavel host
porta = 5000 #numero da porta

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o cliente do socket
cliente.connect((host, porta)) #conecta o cliente em host e porta

a = '3' #valor qualquer fora do menu para entrar no menu na primeira vez
while a != '1' and a != '2': #enquanto o cliente nao escolher um opção valida
        a = raw_input("Escolha a opção desejada \n (1)Enviar Mensagem \t (2)Sair \n") #a recebe valor correspondente a opção selecionada

while a == '1': #enquanto o cliente quiser enviar mensagens
        assunto = raw_input('Digite o assunto (Opcional)\n') #assunto recebe a entrada do teclado (ate o enter)
        msg = raw_input('Digite a mensagem\n') #msg recebe a entrada do teclado (ate o enter)
        cliente.send (assunto)#envia o assunto
        cliente.send (msg) #envia a msg
        a = '3' #valor qualquer fora do menu para entrar no menu na primeira vez
        while a != '1' and a != '2': #enquanto o cliente nao escolher um opção valida
                a = raw_input("Escolha a opção desejada \n (1)Enviar Outra Mensagem \t (2)Sair \n") #a recebe valor correspondente a opção selecionada
cliente.close() #quando msg = x, encerra a conexao

