# 2차 가공 쿼리 
# found.xlsx : 1차가공으로 만들어진 결과 액셀 (여기서 중복값 제거를 해야함)
# final.xlsx(result) : 2차 가공까지 된 액셀파일 

import pandas as pd 

file = "./kcndic/resource/found.xlsx"
target = pd.read_excel(file, engine="openpyxl")

result = []
before = target["headword"][0]
before_pos = target["pos"][0]
before_index = 1
target["exam"][0] = ""
target["exam2"][0] = ""
target["exam3"][0] = ""
target["exam4"][0] = ""
if target["reltype"][0] == r"\N":
    target["reltype"][0] = ""
    target["relword"][0] = ""
    target["relword2"][0] = ""
result.append(target.iloc[0])
for i in range(1,len(target)):
    if target["headword"][i] == before:
        target["headword"][i] = ""
        target["headword2"][i] = ""
        target["headword3"][i] = ""
        target["origin"][i] = ""
        if target["pos"][i] == before_pos:
            target["pos"][i] = ""
            if target["senseNum"][i] <= before_index:
                target["senseNum"][i] = ""
                target["sense"][i] = ""
                target["sense2"][i] = ""
                target["senseKR"][i] = ""
            else: 
                before_index += 1
    else: 
        before = target["headword"][i]
        before_index = 1
        before_pos = target["pos"][i]
    target["exam"][i] = ""
    target["exam2"][i] = ""
    target["exam3"][i] = ""
    target["exam4"][i] = ""
    if target["reltype"][i] == r"\N":
        target["reltype"][i] = ""
        target["relword"][i] = ""
        target["relword2"][i] = ""
    result.append(target.iloc[i])
    
result_df = pd.DataFrame(result)
output_file = "./kcndic/resource/final.xlsx"
result_df.to_excel(output_file, index=False)