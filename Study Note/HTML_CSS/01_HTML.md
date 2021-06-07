# 1. HTML

> Hyper Text Markup Language 의 약자.
>
> 웹 페이지를 작성하기 위한 언어. 웹 컨텐츠의 구조를 정의한다.



## 구조

### 기본 구조 틀

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



### 세부 구조 내용

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

    

