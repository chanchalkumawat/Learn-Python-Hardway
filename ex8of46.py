"""Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True."""
s=raw_input("enter the string\n")
def is_palindrome(s):
    copy=""
    l=len(s)-1
    for n in range(len(s)):
        copy+=s[l]
        l-=1
    if copy==s:
        return True
    else:
        return False
print is_palindrome(s)

