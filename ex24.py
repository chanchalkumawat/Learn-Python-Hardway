def add(a,b):
    if(a==3 and b==4):
        return a+b
    elif(a==5 or b==2):
        return a*b
    elif(not a==5):
        return a**2
    else:
        print "Wrong choice"
m=int(raw_input("enter number"))
n=int(raw_input("enter another number"))
out=add(m,n)
print out
     
