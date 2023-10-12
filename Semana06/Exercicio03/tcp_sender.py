import socket #import biblioteca socket
import sys #import biblioteca sys

TCP_IP = "127.0.0.1" #IP Host
FILE_PORT = 5005 #porta do arquivo
DATA_PORT = 5006 #porta dos dados
buf = 1024 #tamanho do buffer
file_name = sys.argv[1] #nome do arquivo


try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criação do objeto socket especificando o endereço e protocolo
    sock.connect((TCP_IP, FILE_PORT)) #abertura conexão do socket
    sock.send(file_name) #envio do nome do arquivo
    sock.close() #fechamento da conexão

    print ("Sending %s ..." % file_name) #messagem notificação

    f = open(file_name, "rb") #abertura do arquivo em modo de leitura binario
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criação do objeto socket especificando o endereço e protocolo
    sock.connect((TCP_IP, DATA_PORT)) #abertura conexão do socket
    data = f.read() #leitura do conteúdo do arquivo
    sock.send(data) #envio do conteudo

finally:
    sock.close() #fecha conexão
    f.close() #fecha arquivo