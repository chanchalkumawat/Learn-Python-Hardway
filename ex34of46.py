"""Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user, builds a frequency listing of the characters contained in the file, and prints a sorted and nicely formatted character frequency table to the screen."""
def char_freq_table(name):
    a=open(name,'r')
   
    words=a.read()
    d = {}
    for w in words:
      
        print"hii"
       
        #w1=w.replace("\n","")
        d[w]=words.count(w)
        #wordfreq.append(m)
    return d #wordfreq
print char_freq_table("check.txt")

