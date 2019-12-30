import socket
import datetime
# Ben Tilden
# 250959344
# Server_TCP.py created for CS 3357a 2019
# Assignment 2

# Get the current date and time
now = datetime.datetime.now()

# Specify IP address
TCP_IP = '127.0.0.1'
# Specify port number
TCP_PORT = 5005

# Open socket and wait for connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

# Accept connection when one is requested
conn, address = s.accept()

# Establish connection
print('Server Address:', TCP_IP)
print('Client Address:', address)
print("Connection to Client Established, Waiting to Receive Message...")
# Listen for messages
s.listen(1)

# Decode the received message
data = conn.recv(1024).decode()

# If data is not data, ie it has an error, respond with error message
if not data:
    conn.send(str.encode("Error receiving data"))
# If data is equal to the valid command, respond with current date and time
if data == "What is the current date and time?":
    conn.send(str.encode(now.strftime("%m-%d-%Y %H:%M:%S")))
# Else, assume input command was invalid and respond with error message
else:
    conn.send(str.encode("Your question is invalid"))


