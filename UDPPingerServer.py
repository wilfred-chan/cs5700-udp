# UDP Pinger Server 
# We will need the following module to generate randomized lost packets
import random
from socket import *

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 15005))  # binds socket to localhost:15005 since we are Group 5

while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from message
    message, address= serverSocket.recvfrom(2048)
    # Cappitalize the message from the client
    message = message.decode().upper()
    # If rand is less than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
    else:
        serverSocket.sendto(message.encode(), address)
