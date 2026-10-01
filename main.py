import socket
import json

HOST = "socket.cryptohack.org"
PORT = 13379

s = socket.socket()
s.connect((HOST, PORT))

print("Connected!")


data = s.recv(4096)
print("Received:", data.decode())

data = s.recv(4096)
print("Received:", data.decode())

payload = {
    "supported": ["DH64"]
}

message = json.dumps(payload) + "\n"
s.sendall(message.encode())

print("Sent to Bob:", payload)

data = s.recv(4096)
print("Received:", data.decode())

data = s.recv(4096)
print("Received:", data.decode())

payload = {
    "chosen": "DH64"
}

message = json.dumps(payload) + "\n"
s.sendall(message.encode())

print("Sent to Alice:", payload)

while True:
    data = s.recv(4096)

    if not data:
        print("Connection closed")
        break

    print("Received:", data.decode())

