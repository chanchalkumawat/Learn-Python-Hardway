"""Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops."""
a=[]
b=[]
print"Enter elements of first list"
for i in range(0,5):
    n=int(raw_input())
    a.append(n)
print"Enter  elements of second list"
for i in range(0,5):
    n=int(raw_input())
    b.append(n)
def overlapping(a,b):
    for i in a:
        for j in b:
            if i==j:
                return True
    return False
m=overlapping(a,b) 
if m==True:
    print"Have member in comman"
else:
    print"No member comman"
