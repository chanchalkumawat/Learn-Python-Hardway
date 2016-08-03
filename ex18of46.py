"""A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not."""

myPhrase = "The quick brown fox jumps over the lazy dog"

def is_pangram(phrase):
    c = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    phraseLetters = ""
    for char in phrase:
        for letter in alphabet:
            if char == letter and char not in phraseLetters:
                phraseLetters += char
    for char in phraseLetters:
        for letter in alphabet:
            if char == letter:
                c += 1
    if c == 26:
        return True
    else:
        print phraseLetters, alphabet
        return False

print is_pangram(myPhrase)
