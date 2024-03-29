# 210122 Python 에러

> 자주 보이는 에러들을 정리.
>
> 계속 추가될 예정.

## 에러 (Error) 의 종류

1. **Syntax Error**
   * 문법적 오류.
2. **ZeroDivisionError**
   * 수를 0으로 나누려할 때.
3. **NameError**
   * 선언되지 않는 변수일 경우.
   * `... is not defined.`
4. **TypeError**
   * 자료형 타입의 미스 매치 ex) `1 + '4'`
   * 매개변수의 갯수와 입력한 인자의 갯수가 다를 때.
5. **ValueError**
   * 자료형에 대한 타입은 올바른데 잘못된 값이 입력되는 경우.
   * ex) `int('4.5')` : 문법적으로는 문제가 없으나, '4.5' 는 float로 변환할 수는 있지만 int로는 변환하지 못한다. 
6. **IndexError**
   * `list`나 `tuple` 등에서 인덱스를 잘못 입력한 경우.
7. **KeyError**
   * `dictionary`에서 `존재하지 않는 key`를 사용하여 값을 찾으려 한 경우.
8. **ModuleNotFoundError**
   * 패키지명이나 모듈명이 잘못된 경우.
   * 선언한 패키지나 모듈을 찾을 수 없을 때.
9. **ImportError**
   * 모듈 안에 사용하려는 method가 존재하지 않을 때.
10. **KeyboardInterrupt**
    *  `ctrl + c`로 종료한 경우 (Interrupt).
11. **AttributeError**
    * 해당 클래스에 호출한 attribute나 method가 없을 때.

