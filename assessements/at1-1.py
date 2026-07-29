import re

resume = """
Name: Rahul Sharma
Email: rahul123@gmail.com
Phone: 9876543210
Skills: Python, Java, SQL, Machine Learning, NLP
Experience: 3 years
"""

name = re.search(r'Name:\s*(.*)', resume)
email = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', resume)
phone = re.findall(r'\b[6-9]\d{9}\b', resume)
skills = re.findall(r'Python|Java|SQL|Machine Learning|NLP', resume)
exp = re.search(r'(\d+)\s+years', resume)

print("Resume Information")
print("Name:", name.group(1))
print("Email:", email)
print("Phone:", phone)
print("Skills:", skills)
print("Experience:", exp.group(1), "years")

print("\nCandidate Summary")
print("Name:", name.group(1))
print("Experience:", exp.group(1), "years")
print("Skills:", ", ".join(skills))

if int(exp.group(1)) >= 2 and "Python" in skills:
    print("\nEligible for Shortlisting")
else:
    print("\nNot Eligible")
