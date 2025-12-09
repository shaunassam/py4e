###########################
## CHAPTER 9: EXERCISE 5 ##
###########################
# Same as CH09 > ex3 except grab the domain instead of 
# the full email address.

domaindict = dict()
counter = 0

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    if line.startswith("From"):
        if line.startswith("From:"):
            continue
        else:
            line = line.rsplit()
            email = line[1]
            dompos = email.find("@")
            emaillen = len(email)
            domain = email[dompos+1:emaillen]
            if domain not in domaindict:
                domaindict[domain] = 1
            else:
                domaindict[domain] += 1
print(domaindict)