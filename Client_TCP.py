import socket
# Ben Tilden
# 250959344
# Client_TCP.py created for CS 3357a 2019
# Assignment 2

# Specify IP address
TCP_IP = '127.0.0.1'
# Specify port number
TCP_PORT = 5005
# Specify buffer size: maximum about of data to be received at once by socket
BUFFER_SIZE = 1024

# Contact server and establish connection
print ("Attempting to contact server at ",TCP_IP,":",TCP_PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print ("Connection to Server Established")

# User input command
message = input("Enter text command: ")
# Send encoded message to server
s.sendall(message.encode())
# Receive message back no larger than the buffer size
data = s.recv(BUFFER_SIZE)
# Close the client connection
s.close()

# Decode the server message
response = data.decode()
# Validate response
if response == "Your question is invalid":
    print(response)
else:
    print("Current Date and Time -", data.decode())
