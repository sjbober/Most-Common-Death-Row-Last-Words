import matplotlib.pyplot as plt
import numpy as np
from countwords import counts

#creates a sorted list of the last words and then a sorted list of corresponding counts
words = sorted(counts, key=counts.get, reverse=True) #sorts the list of words in descending order (most common words first)
limit = 10
words = words[:limit]

numwords = list()
for i in words:
    numwords.append(counts[i])

def horiz_barchart(yaxis,xaxis):
    #this function creates a horizontal bar chart
    plt.barh(yaxis, xaxis, align='center', alpha=0.5, color=['g','c','c','c','c','c','c','c', 'c','c'], edgecolor = 'k')
    plt.yticks(yaxis)
    plt.xlabel('Number of Occurrences')
    plt.title('Ten Most Frequently Occurring Last Words on Death Row')

    plt.show()

horiz_barchart(words,numwords)
