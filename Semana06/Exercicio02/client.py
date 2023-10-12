import socket #import da biblioteca

HEADER = 64 #definir número de bytes
PORT = 5050 #porta de comunicação
FORMAT = 'utf-8' #formato de decodificação
DISCONNECT_MESSAGE = '!DISCONNECT' #define mensagem
SERVER = "192.168.1.26" #define IP
ADDR = (SERVER, PORT) #variavel de comunicação do servidor a porta ADDR

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #define varievel como classe socket de entrada e saida

client.connect(ADDR) #conexão cliente e ADDR

def send(msg): #função para enviar mensagem ao client
  message = msg.encode(FORMAT) #codifica a mensagem no formato selecionado
  msg_lenght = len(message) #tamanho da string
  send_length = str(msg_lenght).encode(FORMAT) #transforma o tamanho em string e codifica
  send_length += b' ' * (HEADER - len(send_length)) #passa para 64 bytes
  client.send(send_length) #envia o tamanho para o servidor
  client.send(message) #envia a mensagem para o servidor
  print(client.recv(2048).decode(FORMAT)) #decodifica a mensagem e print


send('Hello World!') #envio de mensagens
input()
send("Hello Everyone!")
input()
send("Hello Tim!")
send(DISCONNECT_MESSAGE) #desconexão