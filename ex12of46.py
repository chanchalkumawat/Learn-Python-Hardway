"""Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

****
*********
*******"""
a=3
b=5
c=6
def histogram(a,b,c):
    for i in range(0,a):
        print "*",
    print "\n"
    for i in range(0,b):
        print "*",
    print "\n"
    for i in range(0,c):
        print "*",
    print"\n"
histogram(a,b,c)



