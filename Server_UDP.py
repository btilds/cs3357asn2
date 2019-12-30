import socket
import datetime
# Ben Tilden
# 250959344
# Server_UDP.py created for CS 3357a 2019
# Assignment 2

# Get the current date and time
now = datetime.datetime.now()

# Specify IP address
UDP_IP = '127.0.0.1'
# Specify port number
UDP_PORT = 5005
# Specify buffer size
BUFFER_SIZE = 1024

# Open socket, bind, and wait for connections
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((UDP_IP, UDP_PORT))

# Decode the received message
data, address = s.recvfrom(BUFFER_SIZE)
data = data.decode()

# If data is not data, ie it has an error, respond with error message
if not data:
    s.sendto(str.encode("Error receiving data"), address)
# If data is equal to the valid command, respond with current date and time
if data == "What is the current date and time?":
    s.sendto(str.encode(now.strftime("%m-%d-%Y %H:%M:%S")), address)
# Else, assume input command was invalid and respond with error message
else:
    s.sendto(str.encode("Your question is invalid"), address)


