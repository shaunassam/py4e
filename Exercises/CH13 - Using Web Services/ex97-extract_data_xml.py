####################################################
##             ONLINE ASSIGNMENT #1:              ##
##            Extracting Data from XML            ##
####################################################
# In this assignment you will write a Python program somewhat similar to 
# http://www.py4e.com/code3/xml3.py. The program will prompt for a URL, 
# read the XML data from that URL using urllib and then parse and extract 
# the comment counts from the XML data, compute the sum of the numbers in 
# the file.
# 
# We provide two files for this assignment. One is a sample file where we 
# give you the sum for your testing and the other is the actual data you 
# need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_2335787.xml (Sum ends with 67)

import xml.etree.ElementTree as ET
import urllib.request

input = ""
sumcount = 0

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_2335787.xml')
for line in fhand:
    line = line.decode()
    input += line
#print(input)

tree = ET.fromstring(input)
lst = tree.findall('comments/comment')

for item in lst:
   xmlcount = item.find('count').text
   count = int(xmlcount)
   sumcount += count
print(sumcount)