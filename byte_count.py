#Adds ?d bytes reported in file with matching string
import re, sys

log = sys.argv[1]

input_string = input("Enter string to search for in line (e.g: ` [user] OK UPLOAD `): ")
total_bytes = 0

regex = re.compile(r'(\d+)\s+bytes')
with open(log) as file:
    for line in file:
        if input_string in line:
            search = re.search(regex, line)
            if search:
                bytes_uploaded = int(search.group(1))
                total_bytes += bytes_uploaded

print(total_bytes, " bytes")