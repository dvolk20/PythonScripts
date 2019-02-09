#Python Program to get IP address and hostname

import socket

hostname = socket.gethostname()
IPAddress = socket.gethostbyname(hostname)

print("My computer name is: " + hostname)
print("My IP address is: " + IPAddress)

