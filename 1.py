#client
import socket

SERVER = "127.0.0.1"
PORT = 8081
# Making socket instance
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Connecting to the server
client.connect((SERVER,PORT))
while True:
    inp = input("\nEnter the operation: ")
    if inp == "stop":
        break
    # Sending the input to the server socket using send method
    client.send(inp.encode())
    # Receiving output from server socket
    answer = client.recv(1024)
    print("\nAnswer is: ", answer.decode())
    print("\n Type 'stop' to terminate the process")

client.close()


# server
import socket

# Use localhost IP address and port no.
LOCALHOST = "127.0.0.1"
PORT = 8081
# Calling the server socket method
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST,PORT))
server.listen(1)
print("Server started")
print("Waiting for client request")
# Server socket ready for getting input from the user
clientConnection, clientAddress = server.accept()
print("Client Connected: ",clientAddress)
# msg = ""
# Receiving the data from client and then creating arithmetic operations
while True:
    data = clientConnection.recv(1024)
    msg = data.decode()
    print("Equation received")
    result = 0
    if(msg == 'stop'):
        break
    # Splitting the received equation to calculate the result
    operation_list = msg.split()
    oprd1 = operation_list[0]
    oprd2 = operation_list[2]
    operation = operation_list[1]
    # Changing str to int
    num1 = int(oprd1)
    num2 = int(oprd2)
    if(operation == "+"):
        result = num1 + num2
    elif(operation == "-"):
        result = num1 - num2
    elif(operation == "*"):
        result = num1 * num2
    elif(operation == "/"):
        result = num1 / num2
    # printing the result
    print("The result is: ", result)
    # Sending result to the client
    print()
    print("Sending the result to the client..")
    # Changing int to string and after encoding send output to client
    output = str(result)
    clientConnection.send(output.encode())

clientConnection.close()
