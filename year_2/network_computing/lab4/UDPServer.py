#UDPServer

from socket import *
import time

#create datagram socket
sock = socket(AF_INET,SOCK_DGRAM)

#server ip address and port

hostname = gethostname()
#ip = gethostbyname(hostname)
addr = (hostname,6789)
sock.bind(addr)

while True:

    try:
        
        data,client_addr = sock.recvfrom(1024)

        if data:
            
            #decode message and get date and time
            message = data.decode()
            date_time = time.asctime(time.localtime(time.time()))
            
            #print message to screen
            print("Message received: ",message)

            #open log file and write messaage and date/time
            f = open("log.txt","a")
            f.write("\'" + message + "\'" + " : " + date_time + "\n")
            f.close()

            #convert message to uppercase and encode
            return_msg = message.upper().encode()

            #send return_msg to client
            sock.sendto(return_msg,client_addr)

    except:
        print("ERROR")
