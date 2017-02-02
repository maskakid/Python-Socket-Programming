from socket import *
serverPort = 12000
s1 = socket(AF_INET,SOCK_DGRAM)
s1.bind(('localhost',serverPort))
print "The Server is ready to receive"
while 1:
    message, clientAddress = s1.recvfrom(2048)
    print "Received Message: "+message
    modifiedMessage = message.upper()
    s1.sendto(modifiedMessage, clientAddress)
    print "Message has been modified and sent to client.\n"
    
