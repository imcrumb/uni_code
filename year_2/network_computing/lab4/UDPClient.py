#UDPClient

from socket import *

#takes domain name from user
print("###Enter the domain name below or type \'get\' to get domain name##")
result = input("\nEnter the domain name: ")
if result == "get":
    domain = gethostname()
else:
    domain = result

#obtains ip address of domain and forms server address
server_ip = gethostbyname(domain)
server_addr = (server_ip,6789)

#create datagram socket
sock = socket(AF_INET,SOCK_DGRAM)

#creating and encoding message
message = input("\nPlease type your message: ")
data = message.encode()

try:
    #attempting to send message to server
    sock.sendto(data,server_addr)

    #receives response from server
    data, addr = sock.recvfrom(1024)

    #if data returned decode and print to screen
    if data:
        return_msg = data.decode()
        print("\nMessage Revceived: ",return_msg)
    else:
        print("\nNO DATA RECEIVED FROM SERVER")

finally:
    print("\nCOMPLETE")
    sock.close()

