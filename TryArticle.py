# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:14:00 2016

@author: hectordelacroixdelavalette
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:55:22 2016

@author: hectordelacroixdelavalette
"""
import pickle
# import nltk


path = "/Users/hectordelacroixdelavalette/Desktop/sentimentAnalysis"


inFile1 = open('/Users/hectordelacroixdelavalette/Desktop/sentimentAnalysis/wordFeatures.pickle', 'rb')
word_features = pickle.load(inFile1)
inFile1.close()


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

inFile2 = open('/Users/hectordelacroixdelavalette/Desktop/sentimentAnalysis/my_classifier.pickle', 'rb')
classifier = pickle.load(inFile2)


inFile2.close()

f_0 = open ('/Users/hectordelacroixdelavalette/Desktop/sentimentAnalysis/Test/Article2.txt')
article = f_0.read()

print classifier.classify(extract_features(article.split()))

