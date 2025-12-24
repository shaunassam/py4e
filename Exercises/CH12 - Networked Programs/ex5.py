############################
## CHAPTER 12: EXERCISE 5 ##
############################
# (Advanced) Change the socket program so that it only shows data 
# after the headers and a blank line have been received. Remember that 
# recv receives characters (newlines and all), not lines.
# http://data.pr4e.org/romeo-full.txt

import socket

textdump = ""
charcount = 0

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
    data = data.decode()
    textdump += data
mysock.close

print(textdump)