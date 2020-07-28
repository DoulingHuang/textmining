import string
import re
import csv
import pandas as pd
import string
from collections import Counter

f = open('new.txt', 'r')
test = f.read()
#print(test)
text = test.translate(str.maketrans('', '', string.punctuation))
#print(text)
cop = re.compile("[0-9]") # 匹配不是中文、大小写、数字的其他字符
string1 = cop.sub('', text) #将string1中匹配到的字符替换成空字符
result = string1.replace('\n', '').split(' ')
print(result)
list = []
for i in result:
    if i != '':
        list.append(i)
print(list)

csv_data = pd.read_csv('Flavier.csv',header=None,sep=',', encoding= 'unicode_escape')

desk1 = pd.DataFrame(Counter(list).values(), index=Counter(list).keys(), columns=['dict'])
for i in range(1, 440):
    string1 = csv_data.iloc[i, 1]
    string2 = csv_data.iloc[i, 2]
    text = str(string1).translate(str.maketrans('', '', string.punctuation))
    text_2 = str(string2).translate(str.maketrans('', '', string.punctuation))
    text1 = text.lower().strip() + text_2.lower().strip()
    regex = re.compile('\s+')
    text2 = regex.split(text1)
    print('-------------------')
    print(text2)
    final = []
    count = 0
    for filename in text2:
        for pattern in list:
            if re.fullmatch(filename, pattern):
                print(filename + '++++++++++++++++')
                count += 1
                print(count)
                final.append(filename)
                print(final)
                print(Counter(final))
    title = csv_data.iloc[i, 0]
    print(title)
    desk2 = pd.DataFrame(Counter(final).values(), index=Counter(final).keys(), columns=[title])
    print(desk2)
    desk1 = pd.concat([desk1, desk2], axis=1)
    print(desk1)
    desk1.to_csv('desk2.csv')

