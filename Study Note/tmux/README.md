# tmux 기본 명령어

## 설치

```bash
$ apt-get install tmux
```



## 사용



### 세션 생성

* vscode에서 tmux로 터미널을 새로 열면 자동으로 세션 생성.
* 이 경우, 세션 이름을 직접 설정할 수 없음.

```bash
$ tmux new -s (session_name)
```



### 생성한 세션 리스트

```bash
$ tmux ls
```



### 로컬 종료 후 다시 원하는 세션 들어가기

* vscode에서 tmux 터미널을 열면, 자동으로 새로운 세션이 생성 됨.
* 그냥 bash 창에 명령어 입력하면 원하는 세션 터미널이 열림.

```bash
$ tmux attach -t (session_number or session_name)
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

