"""
    There are two primary uses of the decorator pattern:
        Enhancing the response of a component as it sends data to a second component
        Supporting multiple optional behaviors
"""

import socket
import gzip
from io import BytesIO

def respond(client):
    response = input("Enter a value: ")
    client.send(bytes(response, 'utf8'))
    client.close()

class LogSocket:
    def __init__(self, socket):
        self.socket = socket
    
    def send(self, data):
        print("Sending {0} to {1}".format(data, self.socket.getpeername()[0]))
        self.socket.send(data)
    
    def close(self):
        self.socket.close()

class GzipSocket:
    def __init__(self, socket):
        self.socket = socket
    
    def send(self, data):
        buf = BytesIO()
        zipfile = gzip.GzipFile(fileobj=buf, mode="w")
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getvalue())
    
    def close(self):
        self.socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('',2401))
server.listen(1)
try:
    while True:
        client, addr = server.accept()
        if log_send:
            client = LogSocket(client)
        if client.getpeername()[0] in compress_hosts:
            client = GzipSocket(client)
        respond(client)
finally:
    server.close()