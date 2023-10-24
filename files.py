"""Opening Files"""

from pathlib import Path
path1 = Path('text_file.txt')
# path2 = Path('C:/Users/chand/Downloads/python.txt')  # absolute reference
contents1 = path1.read_text()
# contents2 = path2.read_text()
# print(contents1)
# print(contents2)

"""Splitting Text into List of Lines"""

lines = contents1.splitlines()
print(lines)
print(len(lines))

"""Printing Text File into Lines"""

for line in lines:
    print(line)
