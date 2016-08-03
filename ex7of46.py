"""Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I"
"""
s="helo"


def reverse(s):
    empty=""
    nul=len(s)-1
    for i in range(len(s)):
        slice=s[nul]
        empty+=slice
        nul-=1
    return empty
print reverse(s)
    
    
