# [Python] Python Object Oriented Programming



## 객체

* 속성(attribute) : 변수 (variable)
* 행동(action) : 함수 (method)



## 클래스 

* 클래스(class) : 설계도
* 인스턴스(instance)



### 클래스 선언하기

```python
class Person(object):
    def __init__(self, name : str):
        self.name = name
```

* `class 클래스 이름(상속받는 객체명)`
  * object는 생략 가능.
* 클래스 이름은 **CamelCase**로.
* `__init__` : 생성자
* `__str__` : 객체를 print 할 때 출력할 내용.
* Magic Method 참조
  * [파이썬 더블 언더스코어: Magic Method | Corikachu](https://corikachu.github.io/articles/python/python-magic-method)

### Method 구현하기

```python
class Person(object):
    def walk(self, velocity):
        self.velocity = velocity
```

* `self` 필요.

### 인스턴스 생성

```python
kim = Person('kim')	# argument 지정 필요.
```

* `self` : 생성된 인스턴스. 



## 상속 (Inheritance)

```python
class Student(Person):
    def __init__(self, name, s_id):
        super().__init__(name)
        self.s_id = s_id
```

* `class 클래스 이름(부모 클래스 이름)`
* `super()`로 부모 클래스 참조 가능.



## 다형성 (Polymorphism)

* 같은 이름, 다른 기능의 method.
* 부모 클래스의 method에 `raise NotImplementedError()`를 하면, 자식 클래스에서 만드시 해당 method를 구현해야한다.



## 가시성 (Visibility)

* attribute명에 __를 붙여서 private로 둘 수 있다.
* 외부에서 접근 불가능.

```python
class Person():
	def __init__(self, name):
        self.__name = name		# 외부에서는 __name에 접근 불가능
        
    @property
    def name(self):
        return self.__name
```

```python
kim = Person('kim')
name = kim.name
```

* `@property` decorator로 변수처럼 호출 가능



### Encapsulation

* 캡슐화, 정보 은닉
* 클래스 간의 정보 공유 최소화



## First-class objects

* 일급객체, 함수
* 변수나 데이터 구조에 할당이 가능한 객체
* 파라미터로 전달 가능
* 리턴 값으로 사용 가능
* 파이썬의 모든 함수는 일급함수



## Inner function

* 함수 안에 다른 함수가 존재
* inner function을 return 가능.

```python
def func(text):
    def inner_func():
        print(text)
    return inner_func
```

* inner function을 decorator로 구현.
* decorator에도 argument를 넣을 수 있다.