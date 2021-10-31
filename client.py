from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

numberOfLost = 0

for count in range(10):
    message = 'ping ' + str(count+1)
    clientSocket.sendto(message.encode(), ("", 15005))  # 15005 is the server port
    try:
        message, address = clientSocket.recvfrom(2048)
        print(message.decode())
    except:
        print("Request timed out")
        numberOfLost += 1
clientSocket.close()
