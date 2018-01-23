import socket
import math
UDP_IP = "127.0.0.1"
UDP_PORT = 1459

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP


while True:
    int_input = input("Enter your number here : ") 
    if(isinstance(int_input, int)):   #send integer to server
        sock.sendto(str(int_input), (UDP_IP, UDP_PORT))
        data, server = sock.recvfrom(1024)
        print "received message:",int_input,"! = ",  data ,"\n"
    else:
        print "please enter integer\n"
    

