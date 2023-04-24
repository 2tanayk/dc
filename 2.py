# server
import socket
import threading

host = "127.0.0.1"
port = 9922

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []

def handle_client(client_, address):
    while True:
        msg = client_.recv(1024)
        
        if not msg:
            if client_ in clients:
                print("\nClient {} disconnected.".format(address))
                clients.remove(client_)

            break

        print("\nMessage from Client {}: {}".format(address, msg.decode("utf-8")))

        for c in clients:
            if c != client_:
                msg = "Client" + address + ": " + msg.decode("utf-8")
                c.send(msg.encode("utf-8"))

    client_.close()

while True:
    client, addr = server.accept()
    print("\nClient {} connected..".format(list(addr)[0]))
    clients.append(client)

    thread = threading.Thread(target=handle_client, args=(client, list(addr)[0]))
    thread.start()
    
#client
import socket
import threading

host = "127.0.0.1"
port = 9922

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

print("\nConnected to the server {}".format(host))

def receive_msgs():
    while True:
        try:
            msg = client.recv(1024)
            print(msg.decode("utf-8"))
            print()

        except:
            client.close()
            break

thread = threading.Thread(target=receive_msgs)
thread.start()

while True:
    print()
    message = input()
    client.send(message.encode("utf-8"))
