from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker
from nltk import sent_tokenize
import time
import sys
import csv
import datetime


# USE THIS FUNCTION TO RETURN THE NUMBER OF SPELLING MISTAKES

def Check_spelling(text):
    t = word_tokenize(text)
    spell = SpellChecker()
    # find those words that may be misspelled
    mistakes=0
    for word in t:
        # Get the one `most likely` answer
        correct=spell.correction(word)
        #print(spell.correction(word))
        
        # Get a list of `likely` options
        #print(spell.candidates(word))
        cand=spell.candidates(word)
        if len(cand)>1 or correct != word:
           # print('its a spelling mistake')
            mistakes+=1
    return mistakes





# BELOW THIS IS FOR GRAMMATICAL ERRORS

def Capitalize(text):
    t=word_tokenize(text)
    f=0
    total=0
    for i in t:
        if f==1:
            Cap=i.capitalize()
            if Cap!=i:
                total+=1
        if i=='.':
            f=1
        else:
            f=0
    return total




def check_articles(text):
    count=0
    t=word_tokenize(text)
    num_tokens=len(t)
    vowels=['a','e','i','o','u','A','E','O','U','I']
    for i in range(0,num_tokens):
        if t[i]=='a':
            if t[i+1][0] in vowels:
                count+=1
        if t[i]=='an':
            if t[i+1][0] not in vowels:
                count+=1
    return count


