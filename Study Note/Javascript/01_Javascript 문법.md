# 1. Javascript 문법



## 자료형 (Data Type)

### Primitive Type

> object가 아닌 기본 타입. 변수에 값으로 저장됨.



* 숫자
* `undefined` : 값이 없음. 값을 할당하지 않으면 undefined가 됨.
* `null` : 값이 없음을 나타냄. typeof 사용 시 object로 표현됨.
* `Boolean`



### Reference Type

* object 타입.
* 변수에 참조 값으로 저장.



### Boolean으로의 자동 형변환

| type        |  `false`   |  `true`   |
| :---------- | :--------: | :-------: |
| `undefined` | 항상 false |     X     |
| `null`      | 항상 false |     X     |
| `number`    | 0, -0, NaN |  나머지   |
| `string`    | 빈 문자열  |  나머지   |
| `object`    |     X      | 항상 true |



---



## 변수 선언

|        |    const    |     let     |     var     |
| :----- | :---------: | :---------: | :---------: |
| 재선언 |      X      |      X      |      O      |
| 재할당 |      X      |      O      |      O      |
| 스코프 | 블록 스코프 | 블록 스코프 | 함수 스코프 |

* var는 호이스팅이 발생하므로, 사용하지 않는 것을 권장.

* **호이스팅** : 





---



## 연산자

###  할당 연산자 (`+=`, `-=`, `*=`, `/=`, `++`, `--`)



### 비교 연산자 (`>`, `<`)

* 결과값을 boolean으로 반환.
* 문자열 비교의 경우, 사전 순서가 빠른 것, 소문자보다 대문자가 더 작은 것으로 취급 됨. (ASCII 코드 순이라 생각하면 됨.)
* ex) `'a' > 'b'` : false, `'a' > 'A'` : true



### 동등 비교 연산자 (`==`)

* 두 피연산자가 같은 값으로 되어있는가를 평가. 
* 자동 형변환이 이루어짐.
* ex) `10 == '10'` : true



#### 자동 형변환 예시

* `100 + '100' = '100100'`
* `true + 10 = 11`



### 일치 비교 연산자 (`===`)

* 자동 형변환이 이루어지지 않는 비교 연산자.
* 두 비교 대상의 자료형과 값이 모두 같은 지를 비교.
* 다른 언어에서의 `==`과 같다.



### 논리 연산자 (`&&`, `||`, `!`)

* `and`, `or`, `not`



### 삼항 연산자 (Ternary Operator)

```javascript
(조건)? (참일 경우) : (거짓일 경우)
```



---



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



---



## 반복문

### `while`

```javascript
while (조건) {
    // 실행 코드
}
```

* 블록 스코프 생성.



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

* 블록 스코프 생성.



### `for ... in`

* 객체의 속성을 순회.
* 배열 순회도 가능하지만, 순서대로 순회한다는 보장이 없다.

```javascript
const order = {
	'menu': value1,
	'cost': value2
}

for (let key in order) {
	// ('menu', 'cost')
}
```

* object의 키 값을 순회.
* value 순회 방법 : `(object).values()`
* key, value 모두 순회 : `(object).entries()`

* 블록 스코프 생성.



### `for ... of`

* 배열 순회.

```javascript
const nums = [1, 2, 3, 4, 5]

for (let num of nums) {
    // 1, 2, 3, 4, 5
}
```

* 블록 스코프 생성.



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



### Array Helper Methods

* 배열을 순회하면서 callback 함수를 수행.



#### `forEach`

> 원소를 순회하며 각 원소에 대해 함수를 실행.

```javascript
array.forEach( function (element[, index[, array]]) {
    // 로직 수행
})
```



#### `map`

> 각 원소에 대해 함수를 실행하고, `return` 값으로 이루어진 새로운 배열을 반환.

```javascript
const newArray = array.map( function (element[, index[, array]]) {
    // 로직 수행
    return newElement
})
```



#### `filter`

> callback 함수의 `return` 값이 참인 원소로만 이루어진 배열 반환.

```javascript
const trueArray = array.filter( function (element[, index[, array]]) {
    // 로직 수행
    return (조건)
})
```



#### `reduce`

> 원소를 순회하면서 수행한 로직에서, 누적되는 값을 설정 가능.

```javascript
const finalAcc = array.reduce( function (acc, element[, index[, array]]) {
    // 로직 수행
    return nextAcc
}[, initialValue])
```

* `acc` : 이전 원소에 대한 callback 함수의 return 값.
* `initialValue` : acc의 초기값. 선언하지 않으면 배열의 첫 원소가 할당. (빈 배열에 대해 reduce를 할 경우 에러 발생.)



#### `find`

> 원소들 중 조건에 맞는 값을 반환.
>
> 여러개일 경우 가장 처음 원소를 반환.

```javascript
const trueValue = array.find( function (element[, index[, array]]) {
    // 로직 수행
    return (조건)
})
```



#### `some`

> 원소들 중, 하나라도 조건에 대해 참인 원소가 있으면 `true`를 반환.
>
> 참인 원소가 하나도 없으면 `false`를 반환.

```javascript
const isThereTrue = array.some( function (element[, index[, array]]) {
    // 로직 수행
    return (조건)
})
```



#### `every`

> 원소들이 조건에 대해 모두 참이면 `true`를 반환.
>
> 하나라도 거짓인 원소가 있으면 `false`를 반환.

```javascript
const isEveryTrue = array.every( function (element[, index[, array]]) {
    // 로직 수행
    return (조건)
})
```



---



##  객체

* python의 dictionary와 유사. 
* key는 문자열만 가능.



### 객체 관련 ES6 문법

* key와 value에 할당할 변수의 이름이 같으면 축약 가능.

```javascript
const num1 = 10

// const nums = {
//     num1: num1,
// }

const nums = {
    num1,
}
```



* method 선언 시, function 키워드 생략 가능.

```javascript
const obj = {
//     method1: function () {
//         // code
//     }
    method1() {
        // code
    }
}

obj.method1()
```



* key를 동적으로 생성 가능.

```javascript
const key = 'keyName'
const value = 100

const obj = {
    [key]: value,
}
```



* 객체의 속성을 key와 같은 변수에 할당할 때

```javascript
const obj = {
    key1: 'value1',
    key2: 'value2',
}

const { key1 } = obj
const { key2 } = obj
```



* JSON → 객체 : `JSON.parse()`
* 객체 → JSON : `JSON.stringify()`

