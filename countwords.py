from clean import statements
from commonwords import listwords

counts = dict() #we will count each word that occurs in all the statements and then add the counts to this dictionary
for eachrow in statements:
    words = eachrow.split()
    for word in words:
        if len(word) < 3 : continue #we are not including words that have less than 3 letters in the dictionary
        if word in listwords: #we are not including the top 100 words or stop words in the dictionary
            continue
        counts[word] = counts.get(word,0) + 1
