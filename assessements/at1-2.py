import re

products = [
    "Laptop",
    "Laptop Bag",
    "Gaming Laptop",
    "Mouse",
    "Keyboard",
    "Smart Phone",
    "Phone Case",
    "Bluetooth Speaker",
    "Smart Watch",
    "USB Cable"
]

while True:
    print("\n1.Exact Search")
    print("2.Prefix Search")
    print("3.Suffix Search")
    print("4.Partial Search")
    print("5.Case-Insensitive Search")
    print("6.Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        k = input("Enter keyword: ")
        r = [p for p in products if re.fullmatch(k, p)]
    elif ch == "2":
        k = input("Enter prefix: ")
        r = [p for p in products if re.match(k, p)]
    elif ch == "3":
        k = input("Enter suffix: ")
        r = [p for p in products if re.search(k + "$", p)]
    elif ch == "4":
        k = input("Enter partial keyword: ")
        r = [p for p in products if re.search(k, p)]
    elif ch == "5":
        k = input("Enter keyword: ")
        r = [p for p in products if re.search(k, p, re.I)]
    elif ch == "6":
        break
    else:
        print("Invalid Choice")
        continue

    print("Matching Products:", r)
    print("Total Matches:", len(r))
