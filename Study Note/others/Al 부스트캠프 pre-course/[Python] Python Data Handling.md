# [Python] Python Data Handling

## Comma Separate Value (CSV)

* 콤마로 필드 구분.
* 탭(TSV)이나 빈칸(SSV) 등으로도 구분.
* 통칭하여 Character Separated Value(CSV)라고 함.
* 텍스트 파일임. (노트패드로 열 수 있음.)
* 파일 열 때 encoding 주의 (윈도우는 CP949로 저장. 호환을 위해서는 쓰는 파일은 utf8이 좋다.)

### csv module

* `delimeter` : 데이터 사이를 띄우는 기준.
* `quotechar` : 각 단위 데이터를 감싸는 기준.



## Web

### 정규 표현식 (regular expression)

* 특정 규칙을 가진 문자열 집합 추출

* 문법이 매우 방대함.

  * 정규식 참조 : [정규표현식(Regular Expression)을 소개합니다. (nextree.co.kr)](https://www.nextree.co.kr/p4327/)

  * 정규식 연습장 : http://www.regexr.com/

### re module

* `re,findall(r'정규식', 문자열 데이터)` : 문자열에서 정규식에 해당되는 것을 모두 찾아줌.



## XML (eXtensible Markup Language)

* 마크업 언어, html과 비슷
* 컴퓨터 간에 정보 주고받기에 유용한 저장 방식으로 사용됨.
* 정규표현식으로도 parsing이 가능하지만, 손쉬운 parser들이 개발되어 있음.

### beautifulsoup

* 가장 많이 사용되는 XML parser

 ```python
 from bs4 import BeautifulSoup
 
 # 객체 생성
 soup = BeautifulSoup(문자열 데이터, 'parser(주로 lxml)')
 soup.find_all('태그')
 ```

* `.get_text()` : 태그 안의 내용만 추출해서 반환.
* XML 태그가 다중으로 되어있는 건, 다중으로 코드를 작성해야 함. 
* 가장 바깥 태그만 find로 찾을 수 있음.
* XML 구조를 알 필요가 있음.



## JSON (JavaScript Object Notation)

### json module

* `json.loads(문자열 데이터)` : 문자열 데이터를 dict 타입으로 변환.
* `json.dump(dict 데이터, 쓸 파일)` : json 데이터를 파일에 쓰기.