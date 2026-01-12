############################
## CHAPTER 12: EXERCISE 2 ##
############################
# Change the socket program so it counts the number of characters it has received
# and stops displaying any text after it has shown 3000 characters. Program should
# retrieve the entire document and count the total number of characters and display
# the count at the end of the document.
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

for line in textdump:
    #line = line.strip()
    for i in line:
        charcount += 1

print(textdump[:3000])
print(charcount)