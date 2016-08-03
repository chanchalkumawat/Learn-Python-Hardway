"""An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse, A decimal point = I'm a dot in place. Write a Python program that, when started 1) randomly picks a word w from given list of words, 2) randomly permutes w (thus creating an anagram of w), 3) presents the anagram to the user, and 4) enters an interactive loop in which the user is invited to guess the original word. It may be a good idea to work with (say) colour words only. The interaction with the program may look like so:

>>> import anagram
Colour word anagram: onwbr
Guess the colour word!
black
Guess the colour word!
brown
Correct!"""
def str_permutations(str_input,i):
    if len(str_input) == 1:
        return [str_input]
    comb_list = []
    while i < len(str_input):
        key = str_input[i]
        if i+1 != len(str_input):
            remaining_str = "".join((str_input[0:i],str_input[i+1:]))
        else:
            remaining_str = str_input[0:i]
        all_combinations = str_permutations(remaining_str,0)
        for index,value in enumerate(all_combinations):
            all_combinations[index] = "".join((key,value))
        comb_list.extend(all_combinations)
        i = i+1
    return comb_list
u= str_permutations("ch",0)
print u
user=raw_input("Guess the word:\n")
while(user!=u):
    print"Try again\n"
    put=raw_input("Guess again\n")
print"Godd job"
