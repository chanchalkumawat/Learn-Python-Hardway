"""
Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
"""
#To count length of list
print"enter elements in list:\n"
a=[]
for item in range(0,10):
    num=int(raw_input())
    a.append(num)

def length(b):
    count=0
   
    for n in b:
        count+=1
    return count
m=length(a)
print "Length of list: %d"%m


#To count length of string
a=raw_input("enter string : ") 
def length(a):
    count=0
    for n in a:
        
        count+=1
    return count
n=length(a)
print "Length of string: %d"%n

