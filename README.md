#### 고려대한국어대사전 오픈프로 포멧으로 변경 (ohw)

##### 대사전에서 뽑아야 할 칼럼 (이 칼럼들을 SQL로 뽑아와서 적용하시면 됩니다.)
* eid: 표제어번호(고려대번호)
* ohw: 표제어
* onum (entry 테이블): 어깨번호
* morph: 형태 
* origin: 원어 
* etymol : 어원
* contype: 불규칙 여부
* suppos: 상위품사
* subpos: 하위품사
* onum (explan 테이블): 뜻풀이 번호 
* explan: 뜻풀이
* technic: 전문분야
* pattern: 패턴
* semantic: 의미정보
* restric: 꼴 정보
* theta: 패턴설명 
* example: 용례
* stype: 연관어 종류
* rel_headword(관련어): 연관어 
* conform: 활용형
<br>
<hr>

##### 로직적용 순서
1. [type(표제어 종류) : 단어] 칼럼 추가

<br>
<hr>
🚨 <span style="color:red;"> 아마 하다 오류 나시면 코드를 뜯어고치시거나 변경하셔야 할 것 같습니다.. 그래서 최대한 어떤 로직인지 적어두겠습니다. </span>