import nltk
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["playing", "studies", "running", "happily", "computers", "walking"]

print("Original Word\tStemmed Word")
print("-" * 30)

for word in words:
    print(f"{word}\t\t{stemmer.stem(word)}")
