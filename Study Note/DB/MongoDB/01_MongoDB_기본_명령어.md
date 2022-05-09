# MongoDB 기본 명령어

> 참고 : https://doqtqu.tistory.com/281



## 1. DB 관련 명령어

* DB 리스트 조회

  ```
  show dbs
  ```

  * 하나 이상의 collection을 등록해야 DB name을 볼 수 있다.

* 현재 DB 조회

  ```
  db
  ```

* DB 선택 (및 생성)

  ```
  use (DB_name)
  ```

  * 존재하지 않는 DB name을 입력하면 DB가 생성된다.



## 2. Collection 관련 명령어

* collection 조회

  ```
  show collections
  ```

  * 현재 사용 중인 DB의 컬렉션 조회.

* collection 생성

  ```
  db.createCollection("(collection_name)")
  ```

* collection 삭제

  ```
  db.(collection_name).drop()
  ```



## 3. Document

* 모든 도큐먼트 조회

  ```
  db.(collection_name).find()
  ```

  * 컬렉션 안의 도큐먼트 조회.
  * `.pretty()` : 깔끔한 형태로 출력.

* 

