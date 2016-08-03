"""Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n."""
words=["byee","helllo","hkkkkkk"]
n=6
def filter_long_words(words,n):
      return filter(lambda word:len(word)>n, words)
print filter_long_words(words,n)
    
    
    
    
    
    
    

        
    
