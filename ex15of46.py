"""Write a function find_longest_word() that takes a list of words and returns the length of the longest one."""
list=["word","cat","anamika"]
def find_longest_word(list):
    num=[]
    for word in list:
        w=len(word)
        num.append(w)
    for i in num:
        if num[0]<i:
            num[0]=i
    return num[0]
l=find_longest_word(list)
print "Length of the longest element is : %d"%l

