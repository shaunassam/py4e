############################
## CHAPTER 12: EXERCISE 1 ##
############################
# Change the socket program socket1.py to prompt the user for 
# the URL so it can read any web page.
# http://data.pr4e.org/romeo.txt

import socket

try:
    myurl = input("Enter a URL: ")
    mydomain = myurl.split("/")
    HOST = mydomain[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((HOST, 80))
    endencode = str("HTTP/1.0") + "\r\n\r\n"
    cmd = "GET " + myurl + " " + endencode
    cmd = cmd.encode()
    mysock.send(cmd)
except:
    print("Invalid URL.")
    quit()

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()