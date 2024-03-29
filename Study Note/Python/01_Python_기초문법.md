# 210118 Python 기초 문법

**파이썬의 문법 정리는, 기존에 알고 있던 것과 다른 점을 위주로 정리.**



## 주석 (Comment)

```python
# 한 줄 주석
"""
여러 줄
주석
"""
```



## 코드 라인

* 기본 1줄 1문장 (1 line 1 segment).

* 한 줄 안에 여러 문장을 적을 때는 `;`로 문장을 구분.

  ```python
  print('Hello'); print('World!')
  ```

* 한 문장을 임의로 여러 줄로 적을 때는 `\` 로 연결.

  ```python
  print('Hello\
  World')
  ```

* PEP-8 가이드

  ```python
  # 여러 줄 코드
  print("""Hello
  World""")
  
  # 리스트
  location = [
      '서울', '경기', '인천',
      '강원', '충북', '충남',
      '대전', ...
  ]
  ```

  

## 변수 (Variable)

### 1. 할당 연산자 (Assignment Operator)

* 동시 할당 

  ```python
  x = y = 20		# x = 20, y = 20
  x, y = 10, 20	# x = 10, y = 20	## 갯수를 맞춰야한다.
  x, y = y, x		# x = 20, y = 10	## swap
  ```



### 2. 식별자 (Identifiers)

* 기존의 존재하는 예약어는 사용할  수 없다.

  ```python
  import keyword
  print(keyword.kwlist)		# 예약어의 목록을 볼 수 있다.
  
  del (변수명)				# 앞에서 선언한 변수를 지울 수 있다.
  ```

  

## 데이터 타입 (Data Type)

### 1. 수 (number)

#### 1.1. 정수 (integer)

* 2진수 : `0b` / 8진수 : `0o` / 16진수 : `0x`
* 파이썬은 정수 자료형 오버플로우가 없다.
* 임의 정밀도 산술 (arbitrary-precision arithmetic) 
  * 기존의 방식과 달리, 사용할 수 있는 메모리의 크기가 제한되어 있지 않고 유동적이다. (최대 6 Bytes?)



#### 1.2. 실수, 부동소수점 (float)

* 연산 과정에서 결과값이 정확하게 일치하지 않을 수 있다. 값 비교 시에 주의.

  ```python
  # Example)
  3.5 - 3.12		# 0.3799999999999999 != 0.38
  
  # 비교 처리 방법 
  # 1
  abs(a-b) <= 1e-10
  # 2
  import sys
  abs(a-b) <= sys.float_info.epsilon
  # 3
  import math
  math.isclose(a, b)
  ```



#### 1.3. 복소수 (complex)

```python
a = 3 + 5j
type(a)		# complex
```



### 2. 문자 (String)

* 사용자 입력함수 `input()` 은 숫자를 입력 받아도 string으로 저장된다.

* 문자열은 `+` 연산자로 이어붙일 수 있다.

  ```python
  'Hello' + 'World'		# HelloWorld
  
  a = 'Hello'
  b = 'World'
  a + b					# HelloWorld
  ```

* 문자열은 `* ` 로 반복할 수 있다.

  ```python
  'Hello' * 3		# HelloHelloHello
  ```



#### String interpolation

```python
name = 'Tanaka'
score = 3.5

# str.format()
print('내 이름은 {}. 성적은 {}'.format(name, score))
# f-string
print(f'내 이름은 {name}. 성적은 {score}')		# f를 잊어버리지 않게 주의
# 내 이름은 Tanaka. 성적은 3.5
```

```python
# 출력 형식 지정
import datetime
today = datetime.datetime.now()
print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}')
# '오늘은 21년 01월 18일 Monday'

# 연산
pi = 3.141592
print(f'원주율은 {pi:.4}. 반지름이 2일때 원의 넓이는 {pi*2*2}')
# '원주율은 3.142. 반지름이 2일때 원의 넓이는 12.566368'
```



### 3. Boolean

* 다음은 `False` 로 변환된다. 

  * 0
  * 0.0
  * ()
  * []
  * {}
  * '' 
  * None

* `None` 타입 : 값이 없음을 표현.

  ```python
  print(None ,type(None))		# None <class 'NoneType'>
  ```



### 4. 형변환 (Type conversion, Typecasting)

#### 4.1. 암시적 형변환 (Implicit Type Conversion)

* 파이썬 내부에서 자동으로 형변환을 하는 경우.

  * boolean
  * numbers

  ```python
  # boolean + integer
  True + 5		# 6
  
  # int + float = float
  res = 3 + 6.5		
  print(res, type(res))		# 9.5 <class 'float'>
  
  # int + complex = complex
  res2 = 4 + (2 + 6j)
  print(res2, type(res2))		# (6+6j) <class 'complex'>
  ```



#### 4.2. 명시적 형변환 (Explicit Type Conversion)

* 4.1.을 제외한 모든 경우.
* integer -> string 등



## 연산자 (Operator)

### 1. 산술 연산자

* `//` : 몫

* `**` : 거듭제곱

* 나눗셈 함수 : `divmod(n, m) = (q, r)`

* 양수, 음수 표현 

  ```python
  num = 4
  print(-num)			# -4
  
  num2 = -5
  print(+num2)		# -5
  print(-num2)		# 5
  ```



### 2. 비교 연산자

* `is` : 객체 아이덴티티
* 문자열도 비교 가능.



### 3. 논리 연산자

#### 3.1. 단축평가

```python
# Example)
vowels = 'aeiou'

('a' or 'b') in vowels  	# ('a' or 'b') => 'a', 'a' in vowels => True
('b' and 'a') in vowels  	# ('b' and 'a') => 'a' , 'a' in vowels =>  True
# 암시적 형변환과 괄호 안 우선

('e' in vowels) and ('a' in vowels)	# 'a'와 'e' 둘 다 vowels 안에 있는가
```



### 4. 기타 연산자

* **Concatenation** : 숫자가 아닌 자료형을 `+` 연산자로 합칠 수 있다.

  ```
  'abc' + 'def'		# 'abcdef'
  [1, 2, 3] + [4, 5, 6]		# [1, 2, 3, 4, 5, 6]
  ```

* **Containment Test** : `in` 연산자

  ```python
  # 문자열에 특정 문자가 있는가
  'a' in 'apple'			# True
  
  # 리스트에 특정 원소가 있는가
  4 in [1, 2, 3]			# False
  
  # range 안에 특정 원소가 있는가
  100 in range(1, 5)		# False
  ```

* **Identity** : `is` 연산자, 동일한 object 인가.

* **Indexing** : 값에 접근.

* **Slicing** : 특정 범위를 자름.

  ```python
  a = 'samsung'
  a[0:2]		# 'sa'
  ```



### 5. 연산자 우선 순위

1. `()`을 통한 grouping
2. Slicing
3. Indexing
4. 제곱연산자 `**`
5. 단항연산자 `+`, `-` (음수/양수 부호)
6. 산술연산자 `*`, `/`, `%`
7. 산술연산자 `+`, `-`
8. 비교연산자, `in`, `is`
9. `not`
10. `and`
11. `or`



### 6. 표현식 (Expression) & 문장 (Statement)

* **표현식** : 하나의 값으로 환원될 수 있음.

  ```
  # 하나의 값
  'Hello', 5, 4.3 ...
  
  # 할당문은 그 자체가 표현식
  r = 30
  ```

* **문장** :  파이썬이 실행 가능한 최소한의 코드 단위

