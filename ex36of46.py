"""A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language, the works of an author, or in a single text. Define a function that given the file name of a text will return all its hapaxes. Make sure your program ignores capitalization."""

import re
def hapax(name):
    file = open(name)
    f=file.read().lower()
    words = re.findall('\w+',f)
    freqs = {key: 0 for key in words}
    print freqs
    for word in words:
        freqs[word] += 1
    for word in freqs:
        if freqs[word] == 1:
            print word


hapax('check.txt')
