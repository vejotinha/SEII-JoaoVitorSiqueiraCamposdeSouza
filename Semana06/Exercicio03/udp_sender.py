import socket #import biblioteca socket
import time #import biblioteca time
import sys #import biblioteca sys

UDP_IP = "127.0.0.1" #IP Host
UDP_PORT = 5005 #porta de conexão
buf = 1024 #tamanho do buffer
file_name = sys.argv[1] #nome do arquivo


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #criação do objeto socket especificando o endereço e protocolo
sock.sendto(file_name, (UDP_IP, UDP_PORT)) #vinculo do socket ao endereço ADDR por meio do sendto
print ("Sending %s ..." % file_name) #status

f = open(file_name, "r") #abertura do arquivo em modo de leitura
data = f.read(buf) #leitura do arquivo no tamanho do buffer
while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))): 
        data = f.read(buf) #leitura do arquivo no tamanho do buffer
        time.sleep(0.02) # Give receiver a bit time to save

sock.close() #fecha conexão
f.close() #fecha 