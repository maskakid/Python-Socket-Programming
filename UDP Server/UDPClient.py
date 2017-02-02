from socket import*

serverName = 'localhost'
serverPort = 12000
s = socket(AF_INET,SOCK_DGRAM)
message = raw_input('Input lowercase sentence: ')
s.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = s.recvfrom(2048)
print modifiedMessage
s.close()
