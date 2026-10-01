#!/usr/bin/env python3

import socket
import json

HOST = "socket.cryptohack.org"
PORT = 13379

s = socket.create_connection((HOST, PORT))

buffer = b""


def recv_until_json():
    global buffer

    while True:
        start = buffer.find(b"{")

        if start != -1:
            end = buffer.find(b"}", start)

            if end != -1:
                json_data = buffer[start:end + 1]
                buffer = buffer[end + 1:]

                obj = json.loads(json_data.decode())
                print("RECV JSON:", obj)

                return obj

        data = s.recv(4096)

        if not data:
            raise ConnectionError("Server connection closed")

        print("RAW:", repr(data))
        buffer += data


def send_json(obj):
    data = json.dumps(obj).encode() + b"\n"

    print("SEND:", data.decode().strip())

    s.sendall(data)



alice = recv_until_json()

print("\nAlice supports:")
print(alice["supported"])



send_json({
    "supported": ["DH64"]
})




bob = recv_until_json()

print("\nBob response:")
print(bob)




send_json(bob)


bob = recv_until_json()

print("\nBob response:")
print(bob)

send_json(bob)

next_msg = recv_until_json()

print("\nNEXT MESSAGE:")
print(next_msg)