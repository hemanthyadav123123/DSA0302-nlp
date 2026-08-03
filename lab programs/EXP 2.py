

def fsa(string):
    if string.endswith("ab"):
        print("Accepted")
    else:
        print("Rejected")
text = input("Enter a string: ")

# Function call
fsa(text)
