# 210119 Python Data Types

## Data Container

### 1. 시퀀스 (sequence) 형

*  `ordered` , 순서가 있는 데이터.

* 종류 : `list`, `tuple`, `range`, `string`, `binary`



#### 1.1. 리스트 (list)

* **대괄호**`[]` 사용.

  ```python
  myNumList = [1, 2, 3]
  myStrList = ['서울', '경기', '인천']
  ```

* 리스트 선언 : `list()`

  ```python
  myList = list()		# 빈 list 
  ```



#### 1.2. 튜플 (tuple)

* **소괄호** `()` 사용.

  ```python
  # tuple 선언
  myTuple = (1, 6)
  myTuple2 = 3, 7
  
  # 빈 튜플 선언
  empTuple = ()
  ```

* **수정 불가능** (`immutable`), 읽는 것만 가능.

* `동시 할당`, `swap`에 사용. 내부적으로 사용.

  ```python
  x, y = 2, 9
  x, y = y, x
  ```

* 데이터가 `쌍`으로 있어야 함.

  ```python
  tuple1 = ('apple')		# type(tuple1) => string
  tuple2 = ('apple', )	# type(tuple2) => tuple
  ```

* `indexing` 가능.

  ```python
  myTuple = (2,4)
  print(myTuple[0])		# 2
  ```



#### 1.3. 레인지 (range)

* `range(start, end, step)` : `start` 부터 `end - 1` 까지, `step` 만큼 증가.

* 주로 `list` 로 바꾸어 사용. 

  ```python
  range(5)				# range(0, 5)
  list(range(5))			# [0, 1, 2, 3, 4]
  
  # 0부터 -5까지 내림차순.
  list(range(0, -6, -1))	# [0, -1, -2, -3, -4, -5]
  
  # list의 원소로 range(4)를 넣음.
  [range(4)]		
  ```



#### 1.4. 시퀀스에서 사용할 수 있는 연산자 / 함수

* 포함 여부 확인. (`in`, `not in`)

  ```python
  string = 'string'
  's' in string			# 포함되어 있는가
  'a' not in string 		# 포함되어 있지 않는가
  
  myList = [1, 2, 3, 4, 5]
  7 in myList
  ```

* 연결. (`+`, `*`)

  ```python
  # 이어 붙이기
  [112, 34] + [45, 66]		# [112, 34, 45, 66] : list
  (34, 56) + (5, 98)			# (34, 56, 5, 98) : tuple
  
  # 반복하여 연결하기
  [1, 2] * 3					# [1, 2, 1, 2, 1, 2]
  ```

* `indexing` and `slicing`

  * indexing `[i]` : i 번째 원소에 접근. 0부터 시작.
  * slicing `[i:j:k]` : i 부터 j-1 번째까지의 원소를 k 간격으로 자름.

  ```python
  myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  
  # indexing
  myList[3]			# 4
  
  # slicing
  myList[1:4]			# [2, 3, 4]
  myList[1:6:2]		# [2, 4]
  myList[0::3]		# [1, 4, 7, 10]
  ```

* 그 외
  * `max(container)` : 최댓값
  * `min(container)` : 최솟값
  * `container.count(x)` : x가 몇 개 들어있는가



### 2. 비 시퀀스 (non-sequence) 형

* `unordered` : 순서가 없는 데이터.

* 종류 : `set`, `dictionary`

  

#### 2.1. set

* **중괄호** `{}` 사용. 

* 빈 집합은 {}가 아닌 `set()` 를 사용.

* 수학의 집합과 동일한 연산 가능 (교집합  : `&`, 합집합 : `|`, 차집합 : `-`)

  ```python
  setA = {1, 2, 3}
  setB = {2, 4, 6}
  setEmp = set()	# 빈 집합
  
  # 교집합
  setA & setB		# {2}
  # 합집합
  setA | setB		# {1, 2, 3, 4, 6}
  # 차집합
  setA - setB		# {1, 2}
  ```

* 값의 중복이 없다.

  ```python
  mySet = {1, 2, 3, 3, 2}
  print(mySet)		# {1, 2, 3}
  ```

* `set` 으로 `list` 의 중복값 제거 가능.

  ```python
  listA = [2, 1, 2, 3, 1, 1, 2]
  
  listA = list(set(listA))		# [1, 2, 3]
  ```

  

#### 2.2. dictionary

* **중괄호** `{}` 사용. 

* `{key : value}` 로 선언.

* `key` 는 `immutable` 한 데이터 (`string`, `integer`, `float`,  `boolean`, `tuple`, `range`) 만 사용 가능.

* `value` 는 모든 데이터가 가능.

* 빈 dictionary 는 `{}` 와 `dict()` 를 사용.

* index 가 아니라 `key` 로 접근

  ```python
  # dictionary 선언
  myDict = {'서울': '02', '대전': '042', '구미': '054', '광주': '062'}
  # 빈 dictionary
  empDict1 = {}
  empDict2 = dict()
  ```

* `key` 는 **중복 불가능**.

* `.keys()` 로 key 값들을 확인. 

* `.values()` 로 value 값들을 확인.

* `.items()` 로 dictionary 내용을 확인.

* 각 원소는 `(key, value)`의 tuple이다.

  ```python
  myDict.keys()			# dict_keys(['서울', '대전', '구미', '광주'])
  myDict.values()			# dict_values(['02', '042', '054', '062'])
  myDict.items()			# dict_items([('서울', '02'), ('대전', '042'), ('구미', '054'), ('광주', '062')])
  
  # type이 각각 dict_keys, dict_values, dict_items
  # list로 변환하여 사용 가능.
  ```



#### 2.3. 컨테이너 형변환

* 수의 형변환 : `int < float < complex`, 큰 쪽으로만 변환 가능.

* 모든 자료형은 `string` 으로 변환 가능.

* **list** >> `string`, `tuple`, `set`

  ```python
  l = [1, 2, 3, 4]
  str(l)			# '[1, 2, 3, 4]'
  tuple(l)		# (1, 2, 3, 4)
  set(l)			# {1, 2, 3, 4}
  ```

* **tuple** >> `string`, `list`, `set`

  ```python
  t = (1, 2, 3, 4)
  str(t)			# '(1, 2, 3, 4)'
  list(t)			# [1, 2, 3, 4]
  set(t)			# {1, 2, 3, 4}
  ```

* **range** >> `string`, `list`, `set`, `tuple`

  ```python
  r = range(1, 5)
  str(r)			# 'range(1, 5)'
  list(r)			# [1, 2, 3, 4]
  set(r)			# {1, 2, 3, 4}
  tuple(r)		# (1, 2, 3, 4)
  ```

* **set** >> `string`, `list`, `tuple`

  ```python
  s = {1, 2, 3, 4}
  str(s)			# '{1, 2, 3, 4}'
  list(s)			# [1, 2, 3, 4]
  tuple(s)		# (1, 2, 3, 4)
  ```

* **dictionary** >>

  * `string`
  * **key만 변환** : `list`, `tuple`, `set`

  ```python
  d = {'name': 'kim', 'age': 25, 'address': '서울'}
  str(d)			# "{'name': 'kim', 'age': 25, 'address': '서울'}"
  list(d)			# ['name', 'age', 'address']
  tuple(d)		# ('name', 'age', 'address')
  set(d)			# {'name', 'age', 'address'}
  ```

  

  #### 2.4. mutable vs immutable

  ##### immutable data

  * ***변경 불가능한*** 데이터.

  * `literal(numbers, string, boolean)`, `range`, `tuple`

    ```python
    ### 불가능한 경우 ###
    
    # tuple
    t = (1, 2)
    t[0] = 3
    
    # string
    s = '대한민국'
    s[0] = '머'
    ```

  * 데이터의 ***값에 의한 복사*** 로 복사됨.

    ```python
    num1 = 5
    num2 = num1 
    num2 = 10
    
    print(num1, num2)		# 5, 10
    ```

  

  ##### mutable data

  * ***변경 가능한*** 데이터.

  * immutable 이외의 모든 데이터 (`list` ...).

  * 데이터의 복사가 ***오브젝트의 주소에 의한 복사*** 형태로 이루어짐.

    ```python
    list1 = [1, 2, 3, 4]
    list2 = list1				# list1의  주소가 list2에 복사되어 같은 곳을 가리키게 됨.
    list2[0] = 10
    
    print(list1, list2)			# [10, 2, 3, 4] [10, 2, 3, 4]
    ```

    ```python
    list1 = [1, 2, 3, 4]		# 따로 관리를 하고 싶을 때는
    list2 = list(list1)			# list1과 같은 원소를 갖는 새로운 오브젝트를 만들어주어야 함.
    list2[0] = 10
    
    print(list1, list2)			# [1, 2, 3, 4] [10, 2, 3, 4]
    ```

    

  

  

