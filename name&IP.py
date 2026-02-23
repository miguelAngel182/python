import socket

hostname=socket.gethostname()
IP=socket.gethostbyname(hostname)

print('Your hostname is:',hostname)
print('Your IP is:', IP)