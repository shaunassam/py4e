####################################################
##             ONLINE ASSIGNMENT #2:              ##
##           Extracting Data from JSON            ##
####################################################
# In this assignment you will write a Python program somewhat similar to 
# http://www.py4e.com/code3/json2.py. The program will prompt for a URL, 
# read the JSON data from that URL using urllib and then parse and extract 
# the comment counts from the JSON data, compute the sum of the numbers in 
# the file and enter the sum below:
#
# We provide two files for this assignment. One is a sample file where we give 
# you the sum for your testing and the other is the actual data you need to
# process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_2335788.json (Sum ends with 42)

import json
import urllib.request

input = ""
sumcount = 0

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_2335788.json')
for line in fhand:
    line = line.decode()
    input += line
strlen = len(input)
colpos = input.find('[')
data = input[colpos:strlen-2]
info  = json.loads(data)
for item in info:
    count = int(item['count'])
    sumcount += count
print(sumcount)