# 한한중사전 1차 가공을 위한 쿼리문 (사실 이전에 해둔 버전이 있어 우선 보류한다.)
# -> 아마 대사전 오픈프로 업로드 할 때 다시 수정할 것 같다. 
# 1차 가공 쿼리 : 한한중사전 -> 오픈프로 양식으로 칼럼 통합, 변경 
# 2차 가공 쿼리 : 1차 가공 쿼리에 태운 액셀 파일에서 오류가 나지 않도록 중복값을 제거하는 쿼리 

import pandas as pd

file = "./transform_to_naver/origin_dic_file.xlsx"
df = pd.read_excel(file, engine="openpyxl")

# 표제어 가공
before = df["headword"][0]
print(before)
