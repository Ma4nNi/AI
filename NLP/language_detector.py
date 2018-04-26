from __future__ import division
#from nltk.book import *
from nltk import wordpunct_tokenize
import nltk
from nltk.corpus import words
from nltk.stem import SnowballStemmer
stemmer_sp = SnowballStemmer('spanish')


print(stemmer_sp.stem("YESTERDAY"))
print(stemmer_sp.stem("antier"))
print(stemmer_sp.stem("cuando"))
print(stemmer_sp.stem("puede"))
print(stemmer_sp.stem("ser"))
print(stemmer_sp.stem("celebration"))
print(stemmer_sp.stem("hallo"))
print(stemmer_sp.stem("wie"))


french = nltk.corpus.indian.words
spanish = nltk.corpus.cess_esp.words()

print(french)


