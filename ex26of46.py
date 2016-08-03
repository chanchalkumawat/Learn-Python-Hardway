"""Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well call the reduce() function directly?"""
def max_in_list(list1):
        f = lambda a,b: a if (a > b) else b
        res=reduce(f,list1)
        return res
list1=[]
print "Enter range: "
ran=int(raw_input())
print"Enter elements in list : "
for i in range(0,ran):
    l=int(raw_input()) 
    list1.append(l)      
print "Greatest number is %d"%max_in_list(list1)
