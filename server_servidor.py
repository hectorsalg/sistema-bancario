import socket
from banco import *
import threading

class ClienteThread(threading.Thread):
    """
    Essa classe representa o as conexões para os clientes


    Atributes
    ---------
    clientSock: clientSock
        socket do cliente
    clientAddress: clientAddress
        endereço ip do cliente
    solicitaco: list
        lista com metodo e dados do usuário

    Methods
    ----------
    run():
        recebe solicitação do cliente e envia uma mensagem para o cliente

    """
    def __init__(self, clientSock, clientAddress):
        threading.Thread.__init__(self)
        self.clientSock = clientSock
        self.clientAddress = clientAddress

    def run(self):
        try:
            while True:
                solicitacao = self.clientSock.recv(2048).decode().split("*")
                metodo = solicitacao.pop(0)
                if metodo == 'sair':
                    self.clientSock.close()
                    break
                banco = Banco()
                func = getattr(banco, metodo)
                retorno = func(*solicitacao)
                self.clientSock.send(f'{retorno}'.encode()) 
        except AttributeError:
            print('Error')

class Servidor():

    """
    Essa classe representa o as conexões para os clientes


    Atributes
    ---------
    host: str
        ip do servidor
    port: int
        porta do servidor
    addr: array
        endereço do servidor
    server_socket: socket.socket
        socket do servidor
    novaThread: class
        socket do cliente

    Methods
    ----------
    start():
        recebe solicitação do cliente e envia uma mensagem para o cliente

    """
    
    def __init__(self):
        host = '0.0.0.0'
        port = 5001
        addr = ((host, port))
        self.serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
        self.serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reinicia o socket
        self.serv_socket.bind(addr) #define as portas e quais ips podem se conectar com o servidor
        self.serv_socket.listen(4) #define o limite de conexões

    def start(self):
        while True:
            print("aguardando conexão...")
            client_sock, client_address = self.serv_socket.accept() 
            print(f'Cliente {client_address[0]} conectado.')
            print("aguardando solicitação...")

            novaThread = ClienteThread(client_sock, client_address)

            print("Thread inciada")
            novaThread.start()

c = Servidor()
c.start()