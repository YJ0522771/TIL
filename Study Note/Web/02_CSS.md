# 2. Web - CSS

> HTML에서 스타일, 레이아웃 등을 지정해주는 언어.
>
> 함께 쓰이지만, HTML과는 엄연히 다른 문법을 가지는 다른 언어이다.
>
> 속성(property) 과 값(value) 으로 한 쌍을 이룬다.



### 적용 방법

* 인라인 (`inline`) 방식 

  * tag에 `style` 속성을 추가하여 선언하는 방식.

  * 재사용성이 떨어지고, 코드가 난잡해진다.

    ```html
    <!-- 사용 방법 -->
    <tag style="property: value;">
    	...
    </tag>
    ```

    

* 내부 참조

  * head에 `style` 태그를 추가하여 선언하는 방식.
  * `style` 태그 내부는 html이 아닌 css 문법을 따른다. (주석 형식도 달라짐.) 
  * 인라인 방식에 비해서는 가독성이 좋고, 재사용성이 높다.
  * 같은 스타일을 다른 html에 적용하기는 번거로워, 외부 참조에 비해서는 재사용성이 떨어진다.

* 외부 참조

  * 따로 저장해놓은 css 파일을 `link` 태그를 이용해 불러온다.
  * `link` 태그는 head에 위치.
  * 재사용성이 높고, html 코드 내부가 깔끔해진다.



### 선택자 (Selector)

#### Class 선택자

* 직접 지정한 클래스명에 적용될 스타일을 지정함.

  ```css
  /* 스타일 선언 */
  .class-name1 {
      property1: value1;
      property2: value2;
  }
  ```

  ```html
  <!-- 사용 방법 -->
  <tag class="class-name1 class-name2">
  	...
  </tag>
  ```

* 여러 클래스를 하나의 태그에 선언할 경우 **띄어쓰기**로 구분.
