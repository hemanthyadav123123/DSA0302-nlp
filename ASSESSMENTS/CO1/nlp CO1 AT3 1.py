import re

def validate_email(email):
    pattern = r'^[A-Za-z][A-Za-z0-9._]*@[A-Za-z]+\.(com|org|edu|net|in)$'
    return re.fullmatch(pattern, email) is not None

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!]).{8,}$'
    return re.fullmatch(pattern, password) is not None

def validate_mobile(mobile):
    pattern = r'^[6-9]\d{9}$'
    return re.fullmatch(pattern, mobile) is not None

print("User Registration Validation")

email = input("Enter Email Address: ")
password = input("Enter Password: ")
mobile = input("Enter Mobile Number: ")

if validate_email(email):
    print("Email: Valid")
else:
    print("Email: Invalid")

if validate_password(password):
    print("Password: Valid")
else:
    print("Password: Invalid")

if validate_mobile(mobile):
    print("Mobile Number: Valid")
else:
    print("Mobile Number: Invalid")
