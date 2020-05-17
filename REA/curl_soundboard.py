import sys
import re
lines = []
is_minimal_pair = True

while True:
    line = input()    
    if len(line) == 0:        
        break    
    lines.extend(line.split("<audio"))

urls = [re.sub(".*src=\"(.*)\".*", "\\1", line) for line in lines if "http" in line]

i = 2
for url in urls: 
    number = i // 2    
    fname = url.split("/")[-1].rstrip()    
    fname = fname.replace("1.mp3", ".mp3")    
    if is_minimal_pair:
        print(f"curl -L {url.rstrip()} --output {number:02}-{fname}")    
    else:
        print(f"curl -L {url.rstrip()} --output {fname}")    
    i += 1

