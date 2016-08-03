
a="this is fun"

def translate(a):
    b=""
    for n in a:
        if n==" ":
           b+=" "
           if n=='a' or n=='e' or n=='i' or n=='o' or n=='u':
                b+=n
            
           else:
                b+=n+'o'+n
    return b
m=translate(a)
print m

            
    
