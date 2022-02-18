# Window에서 Linux 사용하기

## VirtualBox

### CentOS7

> 참고 : https://meyouus.tistory.com/150

* 윈도우10에 VirtualBox + CentOS7 설치



### 공유폴더 설정

> 참고
>
> https://koeiking11.tistory.com/entry/Virtual-Box-CentOs-%EA%B3%B5%EC%9C%A0-%ED%8F%B4%EB%8D%94-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0
>
> https://luran.me/480
>
> https://sizzf.tistory.com/28



---



## Docker

### Ubuntu

> Docker에 ubuntu 이미지를 불러와 컨테이너 생성.
>
> 참고 : https://steady-hello.tistory.com/108



### Volume Mount

> 참고 : https://tttsss77.tistory.com/161

```bash
$ docker run -it --name (c_name) -v C:\Users\user\Desktop\share:/home/share (image)
```

* host directory는 해당 os의 경로에 맞춰서.
* ubuntu나 centos는 run할 때, -it를 붙여줘야한다.
