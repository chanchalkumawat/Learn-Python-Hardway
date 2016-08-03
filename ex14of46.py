"""Write a program that maps a list of words into a list of integers representing the lengths of the correponding words."""
list=[]
num=[]
print"Enter words"
list=raw_input().split(',')
print list

for l in list:
      a=len(l)
      num.append(a)
print num,
 
