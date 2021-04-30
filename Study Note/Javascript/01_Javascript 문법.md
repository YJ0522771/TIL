# Practice





## 조건문

### `if, else if, else`

```javascript
if (조건1) {
	// 실행 코드1
} else if (조건2) {
	// 실행 코드2
} else {
	// 실행 코드3
}
```

* 괄호 안에 **블록 스코프** 생성



### `switch`

```javascript
switch (조건) {
	case 결과1: {
		// 실행 코드1
		break
	}
	case 결과2: {
		// 실행 코드2
		break
	}
        
    ...
    
	default: {
		// 조건이 결과1도 결과2도 아닐 경우
	}
}
```

* `break`가 없으면, switch문을 벗어나지 않고 다음 case의 코드도 실행시켜버림.
* `default`는 필수는 아니다.
* **블록 스코프** 생성.



## 반복문

### `for`

```javascript
for (초기화; 조건; 매 반복 후 시행) {
	// 실행 코드
}

// 예시
for (let i = 0; i < 5; i++) {
    // 5번 반복 (0, 1, 2, 3, 4)
}
```



### `for ... in`

* 키 값을 순회

```javascript
const order = {
	'menu': value1,
	'cost': value2
}

for (let key in order) {
	// ('menu', 'cost')
}
```







## 함수

* 선언식

  ```javascript
  function add (n1, n2) {
      return n1 + n2
  }
  ```

* 표현식

  ```javascript
  // 익명 함수 선언
  // sub(n1, n2)로 사용 가능.
  const sub = function (n1, n2) {
      return n1 - n2
  }
  ```



* 함수의 타입 : `function` (`typeof (함수명)`)
* 선언식은 `hoisting`을 발생시킨다.
* 표현식의 `hoisting`은 선언부만 먼저 인식되기 때문에, `undefined`로 인식되어 에러 발생.
* 자바스크립트의 함수는 **일급 객체**에 해당.
  * 변수에 할당 가능.
  * 함수 매개변수로 전달 가능.
  * 함수 반환 값으로 사용 가능.



### Arrow Function

* `function` 키워드 생략 가능.
* 매개변수가 하나 뿐이면, `()` 생략 가능. (선택)
* 내부의 표현식이 하나면, `{}` 생략 가능. `return` 생략 가능. (선택)

```javascript
// const (함수명) = (매개변수명) => (반환값)
const func = name => `My name is ${name}.` 
```





## 배열

* 참조 타입 객체.
* 순서가 있다.
* `[]`를 사용하여 정의함.
* 인덱스는 0부터
* 길이 : `array.length`



### 주요 method

* `.reverse()` : 반대 순서로 정렬.
* `.push(x)` : x를 배열 제일 뒤에 추가.
* `.pop()` : 마지막 원소 제거.
* `.unshift(x)` : x를 배열 가장 앞에 추가.
* `.shift()` : 첫번째 원소 제거.
* `.includes(x)` : x가 해당 배열에 있는 지를 `true / false`로 반환.
* `.indexOf(x)` : 배열에서 가장 처음에 있는 x의 인덱스 반환. 없을 경우 `-1` 반환.
* `.join(separator)` : 배열의 모든 원소를 `separator`로 연결하여 반환. 기본 값은 `,`(쉼표).