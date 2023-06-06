import socket
HOST = '192.168.128.65' # Endereco IP do Servidor
PORT = 5000 # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print ('Para sair use CTRL+X\n')
while True:
    msg = input().encode()
    udp.sendto (msg, dest)
    msg = input()
udp.close()
