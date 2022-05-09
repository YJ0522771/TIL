# Docker compose

> 생활코딩 docker compose
>
> https://www.youtube.com/watch?v=EK6iYRCIjYs



## `docker-compose.yml`

```dockerfile
version: 

services:
	(container1_name):
		image: (image_name)
		volumes:
			-(host_path):(container_path)
		ports:
			-(host_port):(container_port)
		environment: # 환경변수
			(변수 이름):(값)
			...
			
	(container2_name):
		depends_on:
			-(의존 컨테이너 이름)
		image: (image_name)
		environment: # 환경변수
			
```

* 컨테이너 간의 의존 관계가 있는 경우, 의존의 대상이 되는 컨테이너를 먼저 작성.
* docker compose를 사용하면 자동으로 네트워크 생성.



* 실행

  ```bash
  $ docker-compose up
  ```

* 종료

  ```bash
  $ docker-compose down
  ```

  