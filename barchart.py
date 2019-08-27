import matplotlib.pyplot as plt
import numpy as np
from countwords import counts

#creates a sorted list of the last words and then a sorted list of corresponding counts
words = sorted(counts, key=counts.get, reverse=True) #sorts the list of words in descending order (most common words first)
# words = x[:100]
limit = 10
words = words[:limit]

numwords = list()
for i in words:
    numwords.append(counts[i])

def plot_bar_x():
    # this is for plotting purpose
    index = np.arange(len(words))
    plt.bar(index, numwords)
    plt.xlabel('Word', fontsize=13)
    plt.ylabel('Number of Occurrences', fontsize=10)
    plt.xticks(index, words, fontsize=10, rotation=45)
    plt.title('Top %i Most Common Last Words by Texas Inmates' % limit)
    plt.show()


plot_bar_x()
