# 1. Web HTML & CSS

## HTML

> Hyper Text Markup Language 의 약자.
>
> 웹 페이지를 작성하기 위한 언어. 웹 컨텐츠의 구조를 정의한다.



### 1. 구조

#### 기본 구조 틀

````html
<html>
    <head>  
        <title>/* 브라우저 탭의 타이틀 */</title>
        /* 해당 문서의 정보 */
        /* style 혹은 link 로 css 참조 */
    </head>
    <body>
        /* 웹 페이지 본문의 내용 */
        /* 실제로 화면에 나타나는 내용 */
    </body>
</html>
````



#### 세부 구조 내용

* **DOM tree** 구조

* 요소 (element) : **태그**와 **내용**으로 구성.

  ```html
  <tag> 내용 </tag>
  ```

* 시멘틱 태그 : 

* 그룹 컨텐츠

  * `p`
  * `hr`
  * `ol`
  * `pre`
  * `blockquote`
  * `div`

* 텍스트 관련 요소

  * `a`
  * `b`
  * `strong`
  * `i`
  * `em`
  * `span`

* 테이블 관련 요소

  * `tr`
  * `td`
  * `th`
  * `thread`
  * `tbody`
  * `tfoot`
  * `caption`
  * `colspan`

* `<form>`

  * 입력 받은 데이터를 사용하여 서버에 요청해주는 태그.
  * 서버 요청에 사용하기 위해 사용자 입력은 form 태그 안에서 받아야한다.
  * `action` : 요청하는 서버의 주소를 설정하는 **속성 (attribute)**.
  * `method`

* `input` : 데이터 입력 필드. 사용자 입력을 받는다.

  * `label` : 입력 필드의 이름표. `id` 를 사용해 연결하면, label을 클릭하여 입력 필드에 접근할 수 있다.

    ```html
    <label for="name">NAME:</label>
    <input type="text" id="name"> 
    ```

    

## CSS

> HTML에서 스타일, 레이아웃 등을 지정해주는 언어.
>
> 함께 쓰이지만, HTML과는 엄연히 다른 문법을 가지는 다른 언어이다.



#### 적용 방법

* 인라인 (`inline`) 방식 
  * tag에 `style` 속성을 추가하여 선언하는 방식.
  * 재사용성이 떨어지고, 코드가 난잡해진다.
* 내부 참조
  * head에 `style` 태그를 추가하여 선언하는 방식.
  * `style` 태그 내부는 html이 아닌 css 문법을 따른다. (주석 형식도 달라짐.) 
  * 인라인 방식에 비해서는 가독성이 좋고, 재사용성이 높다.
  * 같은 스타일을 다른 html에 적용하기는 번거로워, 외부 참조에 비해서는 재사용성이 떨어진다.
* 외부 참조
  * 따로 저장해놓은 css 파일을 `link` 태그를 이용해 불러온다.
  * `link` 태그는 head에 위치.
  * 재사용성이 높고, html 코드 내부가 깔끔해진다.