from collections import Counter
import re
import pandas as pd
s1 = "This is a pig, and this is a banana"
s2 = "my name is banana my name is banana"
l1 = s1.split()
l2 = s2.split()
print(l1)
print(l2)
aa = []
i = 0
for item in l1:
    if not item in aa:
        aa.append(item)
    if item in aa:
        i += 1
print(aa)
final = []
count = 0
for j in l2:
    filename = j
    for g in aa:
        pattern = g
        if re.fullmatch(filename, pattern) :
            print(filename+'++++++++++++++++')
            count += 1
            print(count)
            final.append(filename)
            print(final)
            print(Counter(final))
desk = pd.DataFrame(Counter(aa).values(), index=aa, columns=['aa'])
print(desk)
desk2 = pd.DataFrame(Counter(final).values(), index=Counter(final).keys(), columns=['final'])
print(desk2)
result = pd.concat([desk,desk2], axis=1)
print(result)