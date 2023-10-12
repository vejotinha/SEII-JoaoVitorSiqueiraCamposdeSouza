import socket #import biblioteca socket
import select #import biblioteca select

UDP_IP = "127.0.0.1" #IP Host
IN_PORT = 5005 #porta de conexão
timeout = 3 #define tempo de parada


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #criação do objeto socket especificando o endereço e protocolo
sock.bind((UDP_IP, IN_PORT)) #vinculo do socket ao endereço ADDR

while True:
    data, addr = sock.recvfrom(1024) # recebe 1024 bytes de dados
    if data:
        print ("File name:", data) #informe nome do arquivo
        file_name = data.strip() #define variavel com nome do arquivo

    f = open(file_name, 'wb') #abertura do arquivo em modo de escrita binario

    while True:
        ready = select.select([sock], [], [], timeout) #segura o código até que um descritor de arquivo esteja pronto
        if ready[0]:
            data, addr = sock.recvfrom(1024) #recebe 1024 bytes de dados enviados
            f.write(data) #escreve os dados no arquivo
        else:
            print ("%s Finish!" % file_name)
            f.close() #fecha o arquivo
            break