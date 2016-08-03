"""Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab")."""
s=raw_input("Enter a string\n")
def char_freq(s):
    dict={}
    for letter in s:
        dict[letter]=dict.get(letter, 0) + 1
    return dict
print char_freq(s)
