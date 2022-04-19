# tmux 기본 명령어

## 설치

```bash
$ apt-get install tmux
```



## 사용



### 세션 생성

* vscode에서 tmux로 터미널을 새로 열면 자동으로 세션 생성.

```bash
$ tmux new -s (session_name)
```



### 기존에 생성된 세션 접속

```bash
$ tmux attach -t (session_name)
```



### 생성한 세션 리스트

```bash
$ tmux ls
```



### 로컬 종료 후 다시 원하는 세션 들어가기

* vscode에서 tmux 터미널을 열면, 자동으로 새로운 세션이 생성 됨.
* 그냥 bash 창에 명령어 입력하면 원하는 세션 터미널이 열림.

```bash
$ tmux attach -t (session_number)
```



### 세션 종료

* tmux 내에서

```bash
$ exit
```



* tmux 밖 (ex. bash)에서

```bash
$ tmux kill-session -t (session_name)
```

