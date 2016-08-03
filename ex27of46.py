"""Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list comprehensions."""
#using for loop
words=["cat","dog","deer"]
def func(words):
    empty=[]
    for l in words:
        m=len(l)
        empty.append(m)
    return empty
print "Length of words :%s"%func(words)
#using map function
ans=map(len, words)
print "Length of words using map:%s"%ans
#using list comprehensions
r=[len(x) for x in words]
print "Length of words using list com: %s"%r
