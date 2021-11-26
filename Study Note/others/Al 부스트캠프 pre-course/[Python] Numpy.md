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