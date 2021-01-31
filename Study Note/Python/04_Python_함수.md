# 210121 Python 함수

## 함수

* `가독성 高`, `재사용 가능`, `유지보수 용이`

* `def`으로 선언. 끝에 `;`를 붙여준다.

  ```python
  def function_name(para1, para2, ...):
      code1
      code2
      ...
      return output
  ```

* 오직 하나의 **객체**만 `return`

* 아무것도 `return`하지 않으면 `None`이 반환된다.

* `return out1, out2`의 형태로 여러 값을 반환시킬 수 있다. 이 경우 반환되는 값은 `tuple` 형태이다 (하나의 튜플 객체).

  ```python
  nums = [5, 4, 7, 1]
  
  a = sorted(nums)		# nums를 sorting 시킨 리스트 객체를 반환
  print(a)				# [1, 4, 5, 7]
  
  b = nums.sort()			# nums를 sorting 시키고 아무것도 반환하지 않는다.
  print(b)				# None
  ```



## 함수의 Input

### 1. 매개변수 (Parameter)

> 입력을 받아 함수 내부에서 사용되는 변수. 



### 2. 전달인자 (Argument)

> 함수를 호출할 때, 전달되는 입력값.



#### 2.1. 위치 인자 (Positional Arguments)

* 함수 선언 시의 매개변수 순서로 값을 전달.
* 기본적으로 위치로 인자를 판단함.



#### 2.2. 키워드 인자 (Keyword Arguments)

* 함수 호출 시, 직접 매개변수명과 전달인자를 함께 명시해 줌.

* 이 때는 순서가 바뀌어도 상관 없다.

* 위치 인자와 혼용할 경우, 반드시 위치 인자 다음에 키워드 인자만 나와야한다.

  ```python
  def mySum(a, b):
      return a + b
  
  mySum(3, 5)				# a = 3, b = 5
  mySum(b = 3, a = 5)		# a = 5, b = 3
  mySum(3, b = 5)			# a = 3, b = 5
  mySum(a = 3, 5)			# error
  mySum(3, a = 5)			# error (a를 위한 여러 인자가 있다.)
  ```

  

#### 2.3. 기본 인자값 (Default Argument Values)

* 함수 선언 시, 기본값을 함께 명시.

* 인자를 전달하지 않을 경우, 기본 인자값을 사용한다.

* 함수 선언 시, 기본 인자값을 사용하는 매개변수는 반드시 사용하지 않는 매개변수의 뒤쪽에 위치해야 한다.

  ```python
  def mySum(a, b = 7):
      return a + b
  
  mySum(3, 5)			# a = 3, b = 5
  muSum(4)			# a = 4, b = 7
  ```



#### 2.4. 가변 인자 리스트 (Arbitrary Argument Lists)

* 몇 개의 인자가 입력될 지 모를 때 사용.
* 매개변수명 앞에 `*` 를 붙여 나타낸다.
* 함수 내부에서는 `tuple` 로 사용된다.
* 함수 선언 시, **맨 마지막** 매개변수로 위치해야한다. 



#### 2.5. 가변 키워드 인자 (Arbitrary Keyword Arguments)

* 임의의 갯수의 **키워드 인자**를 받을 수 있다.

* 매개변수명 앞에 `**`를 붙임.

* 함수 내부에서 `dictionary`로 사용됨.

  ```python
  # 사용 예
  def myDict(**phone):
      return phone
  
  myDict(서울 = '02', 대구 = '053')
  ```




## Scope

* 코드 내부의 공간 (scope).
* `namespace` 라고도 부른다.



### 이름 검색 (Resolution) 규칙

* 코드가 실행될 때 변수의 이름을 찾는 규칙.
* `LEGB rule` : 변수 이름을 찾는 순서.
  * **Local scope**
  * **Enclosed scope** : 상위 함수
  * **Global scope** : 모듈 호출 시, 혹은 선언된 이후부터 인터프리터 (기계어 번역)가 끝날 때까지
  * **Built-in scope** : 파이썬이 실행 된 시점부터 계속 유지



## 재귀함수 (Recursive function)

> 자기 자신을 호출하는 함수.

```python
# 내부적으로 설정된 재귀 횟수 제한 (최대 재귀 깊이)
import sys
sys.getrecursionlimit()
```

* 재귀는 반복문에 비해 변수의 사용을 줄여줄 수는 있으나, 스택 메모리를 더 많이 사용한다.