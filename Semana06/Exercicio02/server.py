import socket #import da biblioteca socket
import threading #import da biblioteca threading

HEADER = 64 #definir número de bytes
PORT = 5050 #porta de comunicação
SERVER = socket.gethostbyname(socket.gethostname()) #define IP local
ADDR = (SERVER, PORT) #variavel de comunicação do servidor a porta ADDR
FORMAT = 'utf-8' #formato de decodificação
DISCONNECT_MESSAGE = '!DISCONNECT' #define mensagem

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #define varievel como classe socket de entrada e saida
server.bind(ADDR) #vincula o socket ao endereço ADDR

def handle_client(conn: socket.socket, addr): #função para configurar a conexão server-client
  print(f'[NEW CONNECTION] {addr} connected.') #mensagem informativa sobre conexão

  connected = True #variavel booleana
  while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT) #definição do numero de bytes

    if msg_length:
      msg_length = int(msg_length) #conversão pra inteiro
      msg = conn.recv(msg_length).decode(FORMAT) #atribuição da mensagem a uma variavel

      if msg == DISCONNECT_MESSAGE: #verificação do conteúdo da mensagem
        connected = False

      print(f'[{addr}] {msg}') #endereço do client

      conn.send('Message received'.encode(FORMAT)) #confirma recebimento
  
  conn.close() #fecha conexão

def start(): #função para administrar conexões
  server.listen() #sonda conexões
  print(f'[LISTENING] Server is listening on {SERVER}') #status do server

  while True: 
    conn, addr = server.accept() #atribuição das conexões do servidor
    thread = threading.Thread(target=handle_client, args=(conn, addr)) #set da thread de conexão com a função handle_client
    thread.start() #partida da thread
    print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}') #conexões ativas

print('[STARTING] server is starting...') #aviso de start do servidor
start() #chama função start