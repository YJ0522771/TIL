# [Python] Numpy

* numerical python
* 파이썬의 고성능 과학 계산용 패키지



* `np.array(시퀀스 타입 데이터, dtype=자료형)` : 배열 생성 (ndarray라 부름.)
* numpy는 **하나의 데이터 타입**으로만 배열에 넣을 수 있음. (리스트와 가장 큰 차이점)
* C의 array를 사용하여 생성. 
  * 메모리 공간에 차례로 할당.
  * 메모리의 용량이 정해져 있음.
  * 연산을 위한 접근성이 좋음.
  * 파이썬은 기본적으로 각 값들이 메모리의 어딘가에 이미 할당되어있고, 리스트를 만들면 그 메모리의 주소들을 순서대로 저장.
* `array.shape` : array의 차원 구성. 예) 3x3x3의 3차원이면 (3, 3, 3)
* `array.dtype` : array의 데이터 타입.
* `array.ndim` : 차원
* `array.size` : element 개수.
* `array.nbytes` : 데이터 용량.



## Handling Shape

* reshape : 데이터의 내용은 같으나 array의 shape를 바꿈.
  * `array.reshape(차원)` ex) `array.reshape(2, 4)`
  * -1 : 기존 array의 사이즈에 맞춰서 값을 자동으로 서정.
* flatten : 다차원 array를 1차원으로 변환.
  * `array.flatten()`



## indexing & slicing

### indexing

* 콤마(,)로 indexting 가능 : array[0] [0] == array[0, 0]



### slicing

* 행과 열을 각각 slicing 가능.
* ex) `array[1:3, 0:2]`



## creation

### `arange`

* `np.arange(시작, 끝, step)`

### `zeros`

* 0으로 채워진 array

* `np.zeros(shape=, dtype=)`

### `ones`

* 1로 채워진 array

### `empty`

* array 공간만 잡아둠

### ones_like, zeros_like, empty_like

* 입력 array와 크기가 같은 array 생성.

### `identify`

* 단위행렬
* `np.identify(n=, dtype)`

###  `eye`

* 대각이 1인 행렬의 시작점 변경 가능.

  * ex) `np.eye(N=3, M=5, k=2)`

  * 0 0 1 0 0

    0 0 0 1 0

    0 0 0 0 1

### `diag`

* 대각선 값을 추출.
* k 지정 가능.
* `np.diag(array)`

### random module

* 시작~끝 범위의 수를 지정한 분포의 확률에 따라 개수만큼 뽑아줌.

* `np.random.uniform(시작, 끝, 개수)` : 균등분포
* `np.random.normal(시작, 끝, 개수)` : 정규분포
* 그 외에도 많음.



## operation 

### 연산

* `array.sum()`  : 합
* `array.mean()` : 평균
* `array.std()` : 표준편차
* `array.var()` : 분산

### axis

* operaion function이 실행될 때 기준이 되는 축.
* ex)  3차원 array : [][][1] [0] [3] => axis 0, 1, 2

### vstack, hstack

* vstack : array를 세로로 붙임.
* hstack : array를 가로로 붙임.

### concatenate

* array를 지정한 축 기준으로 붙임.
* (2D 기준) axis 0 = vstack
* (2D 기준) axis 1 = hstack



## array operation

### element-wise operations

* shape가 같은 array 간의 연산.
* 같은 위치의 element끼리 연산. (+, -, * 등)
* 숫자 연산과 같이 표기 ex) `arr1 * arr2`

### dot product

* `arr1.dot(arr2)`

### transpose

* `arr.transpose()`
* `arr.T`

### broadcasting

* shape이 다른 array 간의 연산
* `array (op) scalar`
  * scalar 값이 array의 모든 element에 연산 적용.
  * ex) [1, 2, 3] + 2 = [3, 4, 5]
* `array (op) array`
  * 자동으로 shape이 같도록 조정하여, 같은 위치 element 끼리 연산.
  * ex) [[0], [1], [2], [3]] + [1, 2, 3] = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]



## comparison

* 비교 연산자에 대해 broadcasting.
* true, false array로 반환
* 원래의 array와 결과의 shape 같다.



* all : `np.all(조건)` : array의 모든 element에 대해 조건이 참일 때 true
* any : `np.any(조건)` : array의 element 중 조건이 참이 되는 것이 있으면 true



* array와 array 비교 : 같은 위치의 element들끼리 비교 연산을 취함.



* `np.logical_and(bool, bool)`
  * bool에는 bool 타입의 array나 조건이 들어갈 수 있음 (반환 값이 bool 타임 array인 것들)
  * or, not도 존재.
* `np.where(조건, 참일 때 값, 거짓일 때 값)`
* `np.where(조건)` : 참인 index 값들 반환.
* `np.isnan(array)`
* `np.isfinite(array)`



* `np.argmax(array)`  : array 내부의 최대값의 **index**.
* `np.argmin(array)` : array 내부의 최소값 **index**.
* axis 설정 가능. 같은 축에서의 최대, 최소값을 찾음.
* `array.argsort()`



## boolean & fancy index

### boolean index

* `array[조건]` : 조건이 참인 element만 추출해서 반환.

### fancy index

* array를 index로 사용.
* index로 사용되는 array는 int 타입이어야함.
* index로 사용되는 array의 element들은 indexing할 array의 크기 범위를 벗어나면 안 됨.



## data i/o

* `np.loadtxt("파일 경로")`
* `np.savetxt("파일 경로", data, delimㅑter='data 구분 기준')`
  * format 지정 가능.
* `array.astype(data type)` : 파일에서 읽어온 array를 데이터 타입 변환하여 반환.
* `np.save()`, `np.load()` : .npy 파일 형식. pickle 형태로 저장.
