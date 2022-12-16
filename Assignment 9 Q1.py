# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 11:11:47 2022

@author: SANJUSHA
"""

# pip install apyori
import numpy  as np
import pandas as pd

# Some modifications are done to the book data in excel and saved as book_new

df=pd.read_csv("book_new.csv")
df.head()
df.info()
df.shape
df.values[0]

# To use Apriori Algorithm the data should be in list
Books=[]
for i in range(0, 2000):
  Books.append([str(df.values[i,j]) for j in range(0, 11)])
Books
type(Books)
len(Books)

from apyori import apriori
rules = apriori(transactions = Books, min_support = 0.01, min_confidence = 0.1, min_lift = 2, min_length = 2, max_length=2)
rules
results=list(rules)
results

def inspect(results):
    book1       = [tuple(result[2][0][0])[0] for result in results]
    book2       = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(book1, book2, supports, confidences, lifts))

resultsdf = pd.DataFrame(inspect(results), columns = ['book1', 'book2', 'Support', 'Confidence', 'Lift'])
resultsdf

resultsdf.nlargest(n=5, columns='Lift')

# import random 
# import matplotlib.pyplot as plt
# Support=rules.to_numpy(columns=['Support'])
# Confidence=rules.to_numpy(columns=['Confidence'])
# for i in range (len(Support)):
    # Support[i]=Support[i]+0.0025*(random.randint(1,10)-5)
    # Confidence[i]=Confidence[i]+0.0025*(random.randint(1,10)-5)
# plt.scatter(supports,confidences,alpha=0.5,marker="*")
# plt.xlabel('Support')
# plt.ylabel('Confidence')
# plt.show()
# plt(rules)


# Inference :
# Greater the lift value greater the association. 
# for min_support = 0.003, min_confidence = 0.2, min_lift = 2, min_length = 2, max_length=2, 14 rules are generated
# Here, ItalArt and ItalAtlas has the highest lift of 9.19

# for min_support = 0.03, min_confidence = 0.2, min_lift = 2, min_length = 2, max_length=2, 8 rules are generated
# Here, ItalArt and ItalCook has the highest lift of 6.81

# for min_support = 0.05, min_confidence = 0.5, min_lift = 2, min_length = 2, max_length=2, 3 rules are generated
# for min_support = 0.05, min_confidence = 0.1, min_lift = 2, min_length = 2, max_length=2, 8 rules are generated
# for min_support = 0.01, min_confidence = 0.1, min_lift = 2, min_length = 2, max_length=2, 13 rules are generated
# Here, also the results were almost same as
# ItalArt and ItalAtlas with 9.19 lift
# ItalArt and ItalCook with 6.81 lift
# ItalAtlas and ItalCook with 5.47 lift

# Changing min length
# for min_support = 0.03, min_confidence = 1, min_lift = 2, min_length = 3, max_length=4, 40 rules are generated
# Here, ItalCook and CookBks has the highest lift of 5.98

# for min_support = 0.003, min_confidence = 0.2, min_lift = 2, min_length = 4, max_length=4, 641 rules are generated
# Here, ItalAtlas and RefBks has the highest lift of 23.34

# for min_support = 0.03, min_confidence = 0.2, min_lift = 2, min_length = 4, max_length=4
# Here, ItalArt and ItalCook has the highest loft of 13.68
