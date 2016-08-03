"""An alternade is a word in which its letters, taken alternatively in a strict sequence, and used in the same order as the original word, make up at least two other words. All letters must be used, but the smaller words are not necessarily of the same length. For example, a word with seven letters where every second letter is used will produce a four-letter word and a three-letter word. Here are two examples:

  "board": makes "bad" and "or".
  "waists": makes "wit" and "ass".

Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that goes through each word in the list and tries to make two smaller words using every second letter. The smaller words must also be members of the list. Print the words to the screen in the above fashion."""
def alternade(text, setAllWords):
    """ returns a tuple containing the two words that form the alternade
        or None if the word is not an alternade
    """
    listA = [];
    listB = [];
    textLength = len(text);
    # prevent selecting character out of range by ensuring string is even
    if textLength % 2:
        textLength += 1
        text = text + " "
    for i in range( 0, len(text), 2 ):
        listA.append(text[i])
        listB.append(text[i+1])
    strA = ''.join(listA).strip()
    strB = ''.join(listB).strip()

    if strA in setAllWords and strB in setAllWords:
        return (strA, strB)
    return None


setAllWords = set([ "ass", "bad", "or", "wit", "dog", "etc..." ])   

print alternade("board", setAllWords)
print alternade("waists", setAllWords)
