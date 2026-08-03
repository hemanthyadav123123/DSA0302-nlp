
def pluralize(noun):
    # Nouns ending with s, x, z, ch, sh
    if noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"
    elif noun.endswith("y") and noun[-2].lower() not in "aeiou":
        return noun[:-1] + "ies"
    else:
        return noun + "s"
word = input("Enter a singular noun: ")
print("Plural Form:", pluralize(word))
