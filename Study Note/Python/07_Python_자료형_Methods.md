# 210127 Python 자료형 Methods 1

> 계속 수정 혹은 추가될 예정.

## String

> string의 특징 : immutable, ordered, iterable

* string methods : https://docs.python.org/ko/3/library/stdtypes.html#string-methods



#### 1.  `.find(x_str)`  

##### `return (index)`, `-1`

* `x`의 첫번째 위치 (인덱스)를 반환.
* **예외처리** : x가 문자열에 존재하지 않으면, `-1`을 반환.



#### 2. `.index(x_str)` 

##### `return (index)`, `ValueError `

* `x`의 첫번째 위치 (인덱스)를 반환.
* x가 문자열에 존재하지 않으면, `ValueError`.



#### 3. `.replace(old_str, new_str[, count_int])`

##### `return (str)`

* `old` 글자를 `new` 글자로 바꾼 문자열을 반환.
* old에 기존 문자열에 없는 글자가 들어오면, 기존 문자열과 같은 문자열을 반환.
* `count`에 지정된 갯수만큼만 글자를 바꾼다.



#### 4. `.strip([chars_str])` , `.lstrip([chars_str])` , `.rstrip([chars_str])`

##### `return (str)`

* 양쪽 (왼쪽`l` 혹은 오른쪽`r`) 끝의 **공백** (`' '` , `\t`, `\n`, `\r` 등)을 제거한 문자열을 반환.
* `chars`에 지정한 글자를 제거한 문자열을 반환.
* chars에 문자열이 입력 되면, chars에 있는 글자 중 하나만 존재해도 제거한다. 

```python
string = '    test_string\n\t'

# 아무 입력도 없으면 공백을 제거
string.strip()			# 'test_string'
string.lstrip()			# 'test_string\n\t'
string.rstrip()			# '    test_string'

string.strip('\t')		# '    test_string\n'

# 입력 된 문자열에 대해 문자 하나하나를 따로 인식히여 제거.
apple = 'apple'
apple.strip('aeiou')	# 'ppl'
```



#### 5. `.split([char_str])`

##### `return (list)`

* **공백** (`' '` , `\t`, `\n`, `\r` 등)을 기준으로 문자열을 분리한 `list`를 반환.
* `char` 가 지정이 되면 이 글자를 기준으로 문자열을 분리.
* 사용자 입력을 여러 개 받을 때, `input()`과 함께 주로 쓰인다.

```python
# 기본형
'1 2 3'.split()				# ['1', '2', '3']

# 구분자(char) 지정
'1,2,3'.split(',')			# ['1', '2', '3']
'01020560159'.split('1')	# ['0', '020560', '59']

# 구분자가 문자열(길이 2 이상)일 경우
'01020560159'.split('01')	# ['', '02056', '59'], 구분자가 양 끝일 경우 빈 str이 들어간다.
```



#### 6. `'seperator_str'.join(iterable)`

##### `return (str)`

* `iterable`의 요소들을 `seperator`로 구분 짓는 하나의 문자열로 합쳐서 반환.

```python
a = [1, 2, 3]

# space로 구분
' '.join(a)				# '1 2 3'
```



#### 7. 문자 변형 (`str` 타입은 변형이 불가능하므로 바뀐 `str`를 반환)

* `.capitalize()` : **맨 앞** 문자를 대문자로 변환.
* `.title()` : **공백**이나 **기호** 직후의 문자를 대문자로 변환.
* `.upper()` : 문자열의 문자를 **모두 대문자**로 변환.
*  `.lower()` : 문자열의 문자를 **모두 소문자**로 변환. 
* `.swapcase()` :  대문자는 소문자로, 소문자는 대문자로 변환.



#### 8. 문자열 검증 

##### `return (bool)`

`.isalpha()`, `.isdecimal()`, `.isdigit()`, `.isnumeric()`, `.isspace()`, `.isupper()`, `.istitle()`, `.islower()`

