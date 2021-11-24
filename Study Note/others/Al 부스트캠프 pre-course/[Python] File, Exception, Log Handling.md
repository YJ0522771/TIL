# [Python] File, Exception, Log Handling

## Exception

* 예상 가능한 예외
* 예상 불가능한 예외

* 사용자가 잘못된 사용을 할 경우 대처 필요



## Exception Handling

* **try ~ except 문법**

```python
try:
    (예외가 발생할 가능성이 있는 코드)
except (except type):
    (예외 발생 시의 대응 코드)
else:
    (예외가 발생하지 않았을 때 실행할 코드)
finally:
    (예외 발생 여부와 상관없이 항상 실행되는 코드)
```

* exception이 발생하여도 코드가 강제로 종료되는 것이 아님.

* 그 다음 기능을 수행.

* except 구문은 여러 개 사용 가능.

* 모든 exception에 대해 => except type = `Exception` : 권장하지 않음.

* 미리 정의된 에러 구문 출력

  ```python
  except (except type) as e:
  	print(e)
  ```

* **raise** : 필요에 따라 강제로 exception을 발생시킴.

  * 프로그램을 종료

  ```python
  raise (excpet type)
  ```

* **assert**

  ```python
  assert (true or false 조건)
  ```

  * false이면 에러 발생시킴.
  * AssertionError



## File Handling

* 종류 : **binary**, **text**

### Python File I/O

```python
f = open('파일 경로', '모드')
f.close()
```

* 파일 열기 모드
  * r : 읽기 모드
  * w : 쓰기 모드
  * a : 추가 모드 (파일의 마지막에 새로운 내용 추가)

* with 구문과 함께 사용

  ```python
  with open('파일 경로', '모드') as f:
      (실행 코드)
  ```

  * with 구문이 끝나면 파일 종료
  * `f.close()`가 필요 없음.

#### 읽기

```python
f = open('파일 경로', 'r')
```

* `read()` : 파일 전체를 하나의 문자열로 반환.

* `readlines()` : 파일 전체를 한 줄 씩으로 된 list로 반환.
* `readline()` : 한 줄만 반환.

#### 쓰기

```python
f = open('파일 경로', 'w', encoding='포맷')
```

* 포맷 : utf8, utf16, CP949...
* utf8이 많이 사용됨.



### os module

* 디렉토리 관리

* `os.mkdir('디렉토리 이름')` : 디렉토리 생성.
* `os.path.exists('디렉토리 이름')` : 디렉토리 존재 여부 검사.
* `os.path.isfile('파일명')` : 파일인 지 여부 검사.
* `os.path.join('디렉토리명', '파일명')` : 해당 디렉토리의 해당 파일 path를 문자열로 반환.

### shutil module

* `shutil.copy('파일명', '붙여넣을 파일의 경로')` : 파일의 내용을 복사, 붙여넣을 파일이 존재하지 않으면 생성.

### pathlib module

* path를 객체로 다룸.

* `pathlib.Path.cwd()` : 현재 작업 디렉토리 경로를 반환

### pickle module

* 데이터, 객체 등의 정보를 다음 실행 시에도 사용할 수 있도록 파일로 저장.
* `.pickle` 파일.
* 영속화(persistence)