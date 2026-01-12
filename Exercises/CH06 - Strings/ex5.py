###########################
## CHAPTER 6: EXERCISE 5 ##
###########################
# `str = 'X-DSPAM-Confidence: 0.8475'`
# Use `find` and string slicing to extract the portion of the string after 
# the colon then use the `float` function to convert the extracted string
# into a floating point number.

str = 'X-DSPAM-Confidence: 0.8475'
strlen = len(str)
colonpos = str.find(':')
newstr = str[colonpos+1:strlen]
flnewstr = float(newstr)
print(flnewstr)
print(type(flnewstr))