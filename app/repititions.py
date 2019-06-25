from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker
from nltk import sent_tokenize
import sys
import csv
import nltk
from nltk.corpus import wordnet
def sent_repitition(t):
    sentence=sent_tokenize(t)
    dict={}
    count=0
    for sent in sentence:
        if sent not in dict:
            dict[sent]=1
        else:
            dict[sent]+=1

    #print(dict)
    return dict

def phrase_rep(t):
    s=''
    text = word_tokenize(t)
    num_tokens = len(text)
    dict={}
    count=0
    for j in 0,num_tokens-3:
        for i in j,j+2:
            s=s+text[i]
        if s not in dict:
            dict[s]=1
        else:
            dict[s]+=1
            
    for key in dict:
        if dict[key]>4:
            count+=dict[key]%4
    
    #print(dict)
    return dict
def check_relevance(t):

    text = word_tokenize(t)
    num_tokens = len(text)
    dict={}
    for i in text:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    max=0
    imp_word=[]
    done=[]
    for i in text:
        if len(i)<5:
            dict[i]=0
    sorted(dict.items(), key=lambda x: x[1], reverse=True)
    #print(dict)
    p=0
    for key in dict:
        if p==10:
            break
        else:
            imp_word.append(key)
            p+=1
            

    #print(imp_word)
    synonyms = [] 
    antonyms = [] 
    for i in range (1,10):
        for syn in wordnet.synsets(imp_word[i]): 
            for l in syn.lemmas(): 
                synonyms.append(l.name()) 
                if l.antonyms(): 
                    antonyms.append(l.antonyms()[0].name()) 
      
    #print(set(synonyms)) 
    #print(set(antonyms))
    count=0

    for i in synonyms:
        for key in dict:
            if key==i and i not in imp_word:
                count+=1
                #print(key,i)
    #print(count)
    return count  # the number of synonyms used in the essay(proper relevant words used)
phrase_rep("""In 1999, I was born in Tundla. Actually, Tundla is not only my city, it is my home. It is located in Firozabad District in Uttar Pradesh. Tundla is situated on NH2 which connects it to nearest major city of Agra, 24 km away, 17 km away from District Firozabad and 5 km away from Etmadpur. It also serves as a major railway junction in North Central Railway zone. Numerous trains ply from capital city New Delhi which is 210 km away. Tundla is very near to Taj Yamuna Expressway. Tundla is well connected to other major cities of the country via regular trains. Due to proximity to Agra and hence the borders of Uttar Pradesh with Rajasthan, Madhya Pradesh states several inter-state bus services also serve the city. Intra-city transport typically consists of Rickshaws and 3-wheelers. It is a town in tundla tahsil of Firozabad district, Uttar Pradesh. In 1901 the population of Tundla was 3044. It was a major junction on the East Indian Railway. Tundla has a rich heritage of British rule. High walled British constructions, huge barracks, a Catholic church built in 1887, an old Jain temple, Kothis (Bungalows) of officers surrounded by sprawling lawns adorn Tundla as the main center of British administration. These old and beautiful British buildings have now been converted into railway quarters.""")