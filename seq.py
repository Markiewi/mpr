import os
import time
from collections import Counter
start = time.time()
all_files = os.listdir(os.curdir)
counter = Counter()
for filename in all_files:
    if filename.endswith(".txt"):
        file = open(filename)
        counter += Counter(file.read().split())
print(counter)
end = time.time()
print(end - start)