#Looks for IP addresses
import re, sys

log = sys.argv[1]
dictionary = {}

regex = re.compile(r'((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.){3}(25[0-5]|(2[0-4]|1\d|[1-9]|)\d)')
with open(log) as file:
    for line in file:
        search = re.search(regex, line)
        if search:
            ip = search.group()
            if ip in dictionary:
                dictionary[ip] += 1
            else:
                dictionary[ip] = 1

count = 0
for i, n in dictionary.items():
    count += 1
    print(f"KEY: {count} || IP: {i} -> AMOUNT: {n}")