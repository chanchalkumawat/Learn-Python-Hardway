#Write a function find_longest_word() that takes a list of words and returns the length of the longest one. Use only higher order functions.
w=["Bye","chanchalkumawat"]
def find_longest_word(w):
    l=map(len,w)
    return max(l)
print"Length of longest word is : %d"% find_longest_word(w)
