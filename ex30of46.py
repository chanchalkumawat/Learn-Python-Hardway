# -*- coding: utf-8 -*-
"""Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and use it to translate your Christmas cards from English into Swedish. Use the higher order function map() to write a function translate() that takes a list of English words and returns a list of Swedish words."""
dic={"merry":"god",
 "christmas":"jul", 
 "and":"och",
 "happy":"gott", 
 "new":"nytt", 
 "year":"år"
}
l=["merry","christmas","and"]
def translate(l):
     return map(lambda key: dic[key],l)
print "List of swedish words for english words are:%s - %s"%(l,translate(l))
