#단순히 표제어에 대한 정보를 SQL에서 다시 뽑기 위한 코드

import pandas as pd 

file = "found.xlsx"
df = pd.read_excel(file, engine="openpyxl")
result = []
for word in df['headword']:
    if word not in result:
        result.append(word)
cnt = 0
with open("headword_list.txt","w") as f:
    for word in result:
        f.writelines("\"" + word+ "\", ")
        cnt += 1
    if cnt == 10: 
        f.write("\n")
        cnt = 0
