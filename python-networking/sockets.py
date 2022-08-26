import socket as sc
import sys

# Making request with Python using sockets

host = 'www.google.com'
port = 80

# Create a socket
print('# Creating socket')
try:
    mysock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
except sc.error:
    print('Failed to create a socket')
    sys.exit()

print('# Getting remote IP address')
try:
    remote_ip = sc.gethostbyname(host)
except sc.gaierror:
    print('Hostname could not be resolved. Exiting...')
    sys.exit()

# Connect to remote server
print(f'# Connecting to server, {host} ({remote_ip}) ')
mysock.connect((remote_ip, port))

# Send data to remote server
print('# Sending data to server')
request = "GET / HTTP/1.0\r\n\r\n"

try:
    mysock.sendall(request.encode())
except sc.error:
    print('Send failed')
    sys.exit()

# Receive data
print('# Receive data from server')
reply = mysock.recv(512)

print(reply.decode())