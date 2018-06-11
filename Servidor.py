# -*- coding: cp1252 -*-
print 'Autores: Denilson Gomes Vaz da Silva e Julio Cesar Rodrigues'
print 'Trabalho de Redes'
print 'Implementação de Sockets\n'
#importação de modulos
import socket
import thread

host = '' # Endereco para o Servidor ouvir
porta = 5000 # Porta que o Servidor esta ouvindo

print 'Servidor esperando conexao' #exibe a mensagem
def conectado(con, cliente): #define conectado
    print 'Conectado por', cliente #exibie a mensagem

    while True: #loop enquanto tiver mensagem
        assunto = con.recv(1024) #recebe o assunto
        msg = con.recv(1024) #recebe a mensagem
        if not msg: break #se nao tiver mensagem, sai do loop
        print 'Cliente:', cliente, 'Assunto:', assunto #exibe a mensagem
        print 'Mensagem: ', msg, '\n' #exibe a mensagem
        
    print 'Finalizando conexao do cliente', cliente, '\n' #exibe a mensagem
    con.close() #finaliza conexao
    thread.exit() #finaliza thread

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o servidor tcp

orig = (host, porta) #orig recebe o ip e a porta

tcp.bind(orig) #inicia o servidor no ip e na porta
tcp.listen(1) #escuta 1 cloiente por vez

while True: #loop infinito
    con, cliente = tcp.accept() #aceita conexao de cliente
    thread.start_new_thread(conectado, tuple([con, cliente])) #inicia nova thread

tcp.close() #encerra o servidor
