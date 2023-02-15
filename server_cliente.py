import socket 

def server_cliente():
    """
    Essa classe representa uma conexao do cliente ao servidor
    """
    ip = 'localhost'
    port = 5001
    addr = ((ip, port)) 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client_socket.connect(addr)
    return client_socket