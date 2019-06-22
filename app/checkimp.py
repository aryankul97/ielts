import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
   

f=open('MyCity.txt').read()
text = word_tokenize(f)
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
print(dict)
p=0
for key in dict:
    if p==10:
        break
    else:
        imp_word.append(key)
        p+=1
        

print(imp_word)
synonyms = [] 
antonyms = [] 
for i in range (1,10):
    for syn in wordnet.synsets(imp_word[i]): 
        for l in syn.lemmas(): 
            synonyms.append(l.name()) 
            if l.antonyms(): 
                antonyms.append(l.antonyms()[0].name()) 
  
print(set(synonyms)) 
print(set(antonyms))
count=0
for s in range (1,10):
    for i in synonyms:
        for key in dict:
            if key==i and imp_word[s]!=i:
                count+=1
print(count)
if count > 100:
    Score=1
elif count>50:
    Score=0.5
else:
    Score=0
print(Score)

