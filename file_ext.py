#Looks for various file extensions

import re, sys

log = sys.argv[1]
dictionary = {}

regex = re.compile(r'\.(7z|ai|apk|avi|bat|bin|bmp|c|cpp|csv|css|dat|deb|dll|dmg|doc|docx|exe|flv|gif|h|html|ico|iso|jar|java|jpeg|jpg|js|json|log|md|mov|mp3|mp4|pdf|php|png|ppt|pptx|psd|py|rar|rb|rpm|sh|sql|svg|tar|txt|wav|xls|xlsx|xml|zip)', re.IGNORECASE)
with open(log) as file:
    for line in file:
        search = re.search(regex, line)
        if search:
            ext = search.group(1).lower()
            if ext in dictionary:
                dictionary[ext] += 1
            else:
                dictionary[ext] = 1

count = 0
for i, n in dictionary.items():
    count += 1
    print(f"KEY: {count} || EXT: {i} -> AMOUNT: {n}")