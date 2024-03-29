# 210120 Python 조건문&반복문

## 조건문 (Conditional Statement)

* 들여쓰기로 블록을 판단.

* `if `, `elif`, `else`

* 조건의 뒤에 반드시 `:` 를 붙일 것.

  ```python
  # 기본 형태
  
  if score >= 90:
      print('A')
  elif score >= 80:
      print('B')
  elif score >= 70:
      print('C')
  elif score >= 60:
      print('D')
  else:
      print('F')
  ```



## 조건 표현식 (Conditional Expression)

* 다른 말로 **삼항 연산자 (Ternary Operator)**라 부른다.

* C언어의 `(조건)? (참일 때):(거짓일 때)` 와 비슷함.

* `(참일 때) if (조건) else (거짓일 때)`

* `:` 가 들어가지 않는다.

  ```python
  # 조건 표현식 형태
  print('홀수') if num % 2 else print('짝수')
  ```



## 반복문 (Loop Statement)

### 1. `while`

```python
# 사용 예

num = input()

s = 0
a = 1
while a <= int(num):
    s += a
    a += 1
    
print(s)
```



### 2. `for`

```python
# 기본 형태
for (변수) in (iterable 객체, list 등):
	(실행코드)
```

* `in (list)`를 하면 리스트의 원소를 순서대로 하나씩 불러온다.

  ```python
  food = ['한식', '중식', '양식', '일식']
  
  for menu in food:		
      print(menu)
      
  # 한식
  # 중식
  # 양식
  # 일식
  ```

* `enumerate(list)` : index와 value를 함께 활용 가능.

  ```python
  food = ['한식', '중식', '양식', '일식']
  
  for i, menu in enumerate(food, start = 1):		# 시작 번호를 기준으로 인덱싱
      print(i, menu)
      
  # 1 한식
  # 2 중식
  # 3 양식
  # 4 일식
  ```

  

### 3. 반복 제어

* `break` : 루프에서 탈출.

* `continue` : 아래의 코드를 실행하지 않고 다음 루프로 넘어감.

* `else` : 반복문이 무사히 종료되었을 때 실행. `break`에 의해 종료되었을 때는 실행되지 않는다.

  ```python
  nums = [1, 2, 3, 4, 5]
  
  # 반복문이 무사히 종료될 경우
  for i in nums:
      if i == 7:
          print(i)
          break
  else:
      print(nums)			
  # [1, 2, 3, 4, 5]
  
  # break에 의해 종료될 경우
  for i in nums:
      if i == 3:
          print(i)
          break
  else:
      print(nums)
  # 3
  ```

* `pass` : 문법적으로 문장이 필요하지만, 프로그램의 할 일이 정해지지 않은 경우. **자리 채우기**.

  ```python
  # continue와 pass의 차이
  nums = [1, 2, 3, 4, 5]
  # continue
  for i in nums:
      if i == 3:
          continue
      print(i, end = ' ')		# 1 2 4 5
     
  # pass
  for i in nums:
      if i == 3:
          pass
      print(i, end = ' ')		# 1 2 3 4 5
  ```

  

