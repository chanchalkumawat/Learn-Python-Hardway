"""Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)"""
list=[]
print"Enter the elements of list"
for m in range(0,5):
        var=int(raw_input())
        list.append(var)
def is_member(a1,list):
    for i in list:
    
        if a1==i:
            return True
    return False
a=int(raw_input("Enter the number or string to be checked \n"))
print is_member(a,list)
    
