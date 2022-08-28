import socket as sc

HOST = '127.0.0.1' # The server's hostname or IP address
PORT = 65432 # The port used by the server

with sc.socket(sc.AF_INET, sc.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello again!')
    data = s.recv(1024)

print(f'Received {data!r}')