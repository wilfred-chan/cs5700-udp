import time
from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
serverHostname = 'localhost'  # for local test
# serveHostname = ''

numberOfLoss = 0
RTTs = []

for count in range(10):
    message = 'ping ' + str(count+1)
    startTime = time.perf_counter()
    clientSocket.sendto(message.encode(), (serverHostname, 15005))  # 15005 is the server port
    try:
        message, address = clientSocket.recvfrom(2048)
        endTime = time.perf_counter()
        RTT = endTime - startTime
        RTTs.append(RTT)
        print(f'{message.decode()} {round(startTime, 6)}\tRTT: {round(RTT, 6)}s')
    except:
        print('Request timed out')
        numberOfLoss += 1
# Stats
average = round(sum(RTTs) / len(RTTs), 5)
print('\nRTT Stats:')
print(f'  Max: {round(max(RTTs), 5)}s\n  Min: {round(min(RTTs), 5)}s\n  Average: {average}s')
print(f'Packet Loss Rate: {100*numberOfLoss/10}%')
clientSocket.close()
