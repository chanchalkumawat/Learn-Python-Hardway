def max_of_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
print"Enter the numbers"
first=int(raw_input())
second=int(raw_input())
third=int(raw_input())
ans=max_of_three(first,second,third)
print "greatest number is :%d"%ans
