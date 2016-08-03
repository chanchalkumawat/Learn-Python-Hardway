"""Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and prints the line to the screen if it is a palindrome."""

def palindrome(name):
    a=open(name,'r')
    m=""
    lines=a.readline()
    
    for c in lines: 
     
        s = c.strip()
        rev=c.strip()[::-1]
        
        if s==rev:
           m+=s
    return m  
    

print palindrome("check.txt")
         
            
                
