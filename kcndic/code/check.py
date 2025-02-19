# 이 코드는 원래 한한중 신규어 총 2000개를 올려야하는데 1000개밖에 들어가지 않아서 나머지 표제어 1000개를 찾기 위해 작성된 코드다.
# alreadly.xlsx : 올라간 1000개
# have_to_check.xlsx :총 올려야 할 표제어 
# found.xlsx(result) : 추가로 올려야 할 표제어 1000개


import pandas as pd 

file1 = "already.xlsx"
file2 = "have_to_check.xlsx"

uploaded = pd.read_excel(file1, engine="openpyxl")
target = pd.read_excel(file2, engine="openpyxl")
# for i in range(len(target)):
#     print(target["headword"][i])
#     cnt += 1
# print(cnt)
# if "알림판" in uploaded['word'].values:
#     print('sex')

result = []
for i in range(len(target)):
    if target["headword"][i] not in uploaded["word"].values:
        result.append(target.iloc[i])
result_df = pd.DataFrame(result)
output_file = "found.xlsx"
result_df.to_excel(output_file, index=False)