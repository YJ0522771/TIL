# Docker image build

> 생활코딩 docker 이미지 만드는 법.
>
> https://www.youtube.com/watch?v=0kQC19w0gTI



## 1. commit

* 현재 만들어진 컨테이너를 이미지로 만든다.
* 원하는 컨테이너를 지정한 이름의 이미지로 만든다.

```bash
$ docker commit (container_name) (image_name)
```



## 2. Docker File

* 이름은 항상 `Dockerfile`로.

```dockerfile
FROM (베이스 image)

RUN (명령어1) && (명령어2) ...
# ex) RUN apt update && apt install -y python3
# 빌드가 되는 시점에 실행되는 명령어

WORKDIR (path)
# 기본 dir
# 해당 path가 없으면 만들어준다.
# CMD의 명령어들도 이 dir을 대상으로 실행된다.

COPY ["host의 파일 이름", "image의 dir"]
# ex) COPY ["index.html", "."]
# host의 Dockerfile과 같은 위치에 있는 index.html을 image의 work dir에 copy

CMD ["명령어를", "띄어쓰기", "기준으로", "분해하여", "작성"]
# ex) CMD ["python3", "-u", "-m", "http.server"] (python 사용 시 -u 옵션을 항상 사용해야함.)
# 컨테이너가 run 될 때 실행되는 것
```

* RUN을 여러 번 써도 되지만, RUN 하나 당 레이어가 하나 씩 실행되기 때문에 `&&`를 통해 여러 명령어를 연결시켜 사용해주면 좋다.

* RUN은 image에, CMD는 container에 반영되는 것이라 생각하면 됨.

* `docker run` 명령어 마지막에 실행되길 원하는 명령어를 넣으면 CMD의 내용이 덮어써짐. CMD 대신에 실행.

  * ex)

  ```bash
  $ docker run -p 8888:8000 --name (container_name) (image_name) [명령어]
  ```

  * 이 경우 CMD에 지정한 명령어가 아닌, 뒤에 작성한 명령어가 실행.



## 3. build

```bash
$ docker build -t (image_name) (path)
```

* `path` : docker 파일과 이미지 생성 시 함께 사용할 파일들 위치.