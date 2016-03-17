# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 17:55:22 2016

@author: hectordelacroixdelavalette
"""
import nltk
import pickle
import os.path as op

path = "/Users/hectordelacroixdelavalette/Desktop/sentimentAnalysis"

step = 16

###############################################################################
# Load data
print("Loading dataset")

from glob import glob
filenames_neg = sorted(glob(op.join(path, 'train', 'neg', '*.txt')))
filenames_pos = sorted(glob(op.join(path, 'train', 'pos', '*.txt')))


X_neg = []
for text in filenames_neg:
    X_neg.append((open(text).read(),'negative'))

X_pos = []
for text in filenames_pos:
    X_pos.append((open(text).read(),'positive'))

X = []
for (words, sentiment) in X_neg + X_pos:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3] 
    X.append((words_filtered, sentiment))
  

def get_words_in_corpus(X):
    all_words = []
    for (words, sentiment) in X:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features    
    
word_features = get_word_features(get_words_in_corpus(X))

f1 = open('wordFeatures.pickle', 'wb')
pickle.dump(word_features, f1)
f1.close()

    
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


training_set = nltk.classify.apply_features(extract_features, X)

classifier = nltk.NaiveBayesClassifier.train(training_set)

f2 = open('my_classifier.pickle', 'wb')
pickle.dump(classifier, f2)
f2.close()



