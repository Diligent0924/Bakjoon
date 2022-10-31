import re

match = re.compile('ca{2,5}t')
ex = "cat"
a = match.fullmatch(ex)
print(a)