import socket #import biblioteca socket

TCP_IP = "127.0.0.1" #IP Host
FILE_PORT = 5005 #porta do arquivo
DATA_PORT = 5006 #porta dos dados
timeout = 3 #define tempo de parada
buf = 1024 #tamanho do buffer


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criação do objeto socket especificando o endereço e protocolo
sock_f.bind((TCP_IP, FILE_PORT)) #vinculo do socket ao endereço ADDR
sock_f.listen(1) #sonda as conexões possivel

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criação do objeto socket especificando o endereço e protocolo
sock_d.bind((TCP_IP, DATA_PORT)) #vinculo do socket ao endereço ADDR
sock_d.listen(1) #sonda as conexões possivel


while True:
    conn, addr = sock_f.accept() #atribuição das conexões do servidor
    data = conn.recv(buf) #define o tamanho da mensagem
    if data:
        print ("File name:", data) #print nome do arquivo
        file_name = data.strip() #remoção dos bytes inicial e final

    f = open(file_name, 'wb') #abertura do arquivo em modo de escrita binario

    conn, addr = sock_d.accept() #atribuição das conexões do servidor
    while True:
        data = conn.recv(buf) #define o tamanho da mensagem
        if not data:
            break
        f.write(data) #escreve os dados no arquivo

    print ("%s Finish!" % file_name) #status
    f.close() #fecha o arquivo