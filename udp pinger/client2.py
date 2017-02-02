# -*- coding: utf-8 -*-
from socket import *
from datetime import datetime                                   # needed for my timeout system

def main():
    serverName = 'localhost'                                    # destination server is localhost
    serverPort = 12000                                          # destination port number
    counter = 0;                                                # number of pings starts at 0

    message = raw_input()                                       # prompt for user's message

    while counter < 10:                                         # while counter less than 10
        counter = counter +1                                    # add one to counter aka pings
        mainSocket = socket(AF_INET,SOCK_DGRAM)                 # create socket

        try:
            mainSocket.settimeout(1.0)                          # timeout after 1 second
            startTime = datetime.now()                          # start time is current time at declaration

            mainSocket.sendto(message,(serverName, serverPort)) # send the message
            modifiedMessage, serverAddress = mainSocket.recvfrom(1024)  # modified message is the message it gets back
            endTime = datetime.now()                            # end time is current time at declaration

        except timeout:                                         # if timeout
            print ('PINg ' +str(counter)+' '+ str(startTime)+ ': Request timed out!') # print timeout mssg
            mainSocket.close()                                  # close socket
        else:                                                   # else print PING num Start Time Returned Message and RTT
            print ('PING ' +str(counter)+' '+ str(startTime)+': Returned: ' + modifiedMessage.decode('ascii') + ' after '+ str(endTime-startTime))

    mainSocket.close()                                          #close socket
    pass

if __name__ == '__main__':
    main()
