#Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
list=["abcd","chanchal","aghhhhhhhhdfshfdfdfg"]
n=5
def filter_long_words(list,n):
    num=[]
    for l in list:
        w=len(l)
        if w>n:
            num.append(l)
    return num
print filter_long_words(list,n)
        
    
