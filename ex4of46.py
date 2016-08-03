#Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
def check(c):
    if c=='a'or c=='A' or c=='e' or c=='E' or c=='i' or c=='I' or c=='o' or c=='O' or c=='u' or c=='U':
        return True
    else:
        return False
z=raw_input("Enter the character :")
print check(z)
        
