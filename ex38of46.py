"""Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens)."""
def length(name):
    s=0
    f=open(name)
    obj=f.read()
    count=len(obj.split())
    for n in obj.strip().replace(" ",""):                                   
        l=len(n)
        s+=l
    return avg=s/count
print length("check.txt")

