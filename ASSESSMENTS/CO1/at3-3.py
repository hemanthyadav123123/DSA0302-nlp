import re

text = """
Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing
Python programming is useful for NLP applications.
"""

def search_date(text):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    return re.findall(pattern, text)

def search_phone(text):
    pattern = r'\b[6-9]\d{9}\b'
    return re.findall(pattern, text)

def search_hashtag(text):
    pattern = r'#[A-Za-z0-9_]+'
    return re.findall(pattern, text)

def search_mention(text):
    pattern = r'@[A-Za-z0-9_]+'
    return re.findall(pattern, text)

def search_prefix(text, prefix):
    pattern = r'\b' + re.escape(prefix) + r'\w*'
    return re.findall(pattern, text, re.IGNORECASE)

def search_suffix(text, suffix):
    pattern = r'\b\w*' + re.escape(suffix) + r'\b'
    return re.findall(pattern, text, re.IGNORECASE)

def search_word(text, word):
    pattern = r'\b' + re.escape(word) + r'\b'
    return re.findall(pattern, text, re.IGNORECASE)

print("----- TEXT -----")
print(text)

while True:
    print("\n----- SMART PATTERN MATCHING ENGINE -----")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Search Word")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\nMatching Dates:", search_date(text))

    elif choice == "2":
        print("\nMatching Phone Numbers:", search_phone(text))

    elif choice == "3":
        print("\nMatching Hashtags:", search_hashtag(text))

    elif choice == "4":
        print("\nMatching Mentions:", search_mention(text))

    elif choice == "5":
        prefix = input("Enter prefix: ")
        print("\nMatching Prefix Words:", search_prefix(text, prefix))

    elif choice == "6":
        suffix = input("Enter suffix: ")
        print("\nMatching Suffix Words:", search_suffix(text, suffix))

    elif choice == "7":
        word = input("Enter word: ")
        print("\nMatching Words:", search_word(text, word))

    elif choice == "8":
        print("\nExiting program...")
        break

    else:
        print("\nInvalid choice. Please try again.")
