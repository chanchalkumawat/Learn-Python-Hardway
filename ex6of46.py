"""Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24."""
a=[]
print"Enter elements in list"
for item in range(1,4):
    num=int(raw_input())
    a.append(num)
def sum(a):
    s=0
    mul=1
    for item in a:
        s=s+item
        mul=mul*item
    return s,mul
m,n=sum(a)  
print "sum of numbers : %d "%m
print"Multiplication of digits : %d"%n



