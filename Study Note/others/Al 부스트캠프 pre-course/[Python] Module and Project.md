# [Python] Module and Project

## Module

* 프로그램의 작은 조각들

* 모듈이 모여 하나의 프로그램

* .py 파일 => import로 불러옴.

  * import를 하면 .py 안에 있는 모든 코드가 메모리에 로드.

    ```python
    def func():
        return 1
    
    print('hello')
    ```

    다음과 같은 코드의 모듈을 호출하면, import를 하여 메모리에 올림 => hello 출력.

    `if __name__ == '__main__'` 필요.

  * 같은 directory 안에 있어야 함. (상대경로)



## Namespace

* 모듈 안에는 함수나 클래스 등이 존재.
* 호출 범위를 지정.

#### Alias 설정 - 모듈의 별칭

```python
import module as mod
```

#### 특정 함수나 클래스만 호출

```python
from module import function
```

#### 모든 함수나 클래스 호출

```python
form module import *
```



## Package

* 코드의 묶음

* 다양한 모듈들의 모음

* *폴더마다* `__init__.py`를 생성.

  * 현재 폴더가 패키지임을 알려줌.
  * 초기화 스크립트
  * 하위 폴더와 모듈 모두 포함.
  * 파이썬 3.3 이상부터는 없어도 패키지로 인식함.

  ```python
  # __init__.py
  
  __all__ = ['module1', ... (해당 폴더의 사용할 모듈 이름들)]
  
  from . import module1
  ...
  ```

* `__main__.py` : 패키지를 사용하는 메인 프로그램

  ```python
  if __name__ == '__main__':
      (main code)
  ```

* package 이름만으로 호출 가능

  * `$ python (패키지 이름)` : 해당 패키지의 `__main__.py`가 실행



## 가상환경 설정

* 대표 도구 : **virtualenv**, **conda**
* pip는 컴파일 된 C코드들의 포함되지 않는 경우가 있음.
* windows에서는 conda가 유용

### conda 가상환경

* 가상환경 생성

```bash
$ conda create -n (가상환경 이름) python=(파이썬 버전)
```

* 가상환경 실행

```bash
$ conda activate (가상환경 이름)
```

* 가상환경 해제

```bash
$ conda deactivate
```

* 패키지 설치

```bash
$ conda install (패키지 이름)
```

* 파이썬으로 작성되지 않은 패키지들의 컴파일된 파일을 자동으로 설치





