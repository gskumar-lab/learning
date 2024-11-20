import re

text = "The quick brown fox pick "
pattern = r"ic"

find = re.findall(pattern, text)
if find:
    print("Pattern found:", find)
else:
    print("Pattern not found")

