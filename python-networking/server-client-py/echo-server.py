import socket as sc

HOST = "127.0.0.1" # Standard loopback interface (localhost)
PORT = 65432 # Non-privilaged ports are > 1023, dynamic/private ports are 49152 to 65535

with sc.socket(sc.AF_INET, sc.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    
    with conn:
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)