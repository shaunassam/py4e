###########################
## CHAPTER 8: EXERCISE 1 ##
###########################
# Write a function called "chop" that takes a list
# and modifies it, removing the first and last elements
# and returns `None`. Then write a function called "middle"
# that takes a list and returns a new list that contains 
# all but the first and last elements.

def chop(alist):
    lastit = len(alist) - 1
    alist[lastit] = None
    alist[0] = None
    return alist

def middle(alist):
    lastit = len(alist) - 1
    midlist = alist[1:lastit]
    return midlist


mylist = ['a', 'b', 'c', 'd', 'e']
print(mylist)
choplist = chop(mylist)
print("Using `chop` function")
print(choplist)

middlelst = middle(mylist)
print("Using `middle` function")
print(middlelst)