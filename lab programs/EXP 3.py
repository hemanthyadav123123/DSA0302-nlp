import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


nltk.download('punkt')
nltk.download('punkt_tab')

stemmer = PorterStemmer()
text = input("Enter a sentence: ")
words = word_tokenize(text)

print("\nMorphological Analysis (Stemming):")
for word in words:
    print(word, "->", stemmer.stem(word))
