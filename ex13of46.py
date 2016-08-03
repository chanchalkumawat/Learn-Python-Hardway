"""The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one."""
list=[]
a=int(raw_input("Enter the range of the list \n"))
print"Enter elements in list \n"
for i in range(0,a):
    m=int(raw_input())
    list.append(m)
def max_in_list(list):
   
    myMax = list[0]
    for num in list:
        if myMax < num:
            myMax = num
    return myMax
n=max_in_list(list)
print "Greatest element is %d"%n
