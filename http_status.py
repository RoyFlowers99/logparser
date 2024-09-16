#Looks for HTTP status codes
import re, sys

log = sys.argv[1]
dictionary = {}

regex = re.compile(r'(?<=\s)[1-5][0-9]{2}(?=\s)')
with open(log) as file:
    for line in file:
        search = re.search(regex, line)
        if search:
            status = search.group()
            if status in dictionary:
                dictionary[status] += 1
            else:
                dictionary[status] = 1

count = 0
for i, n in dictionary.items():
    count += 1
    print(f"KEY: {count} || STATUS: {i} -> AMOUNT: {n}")