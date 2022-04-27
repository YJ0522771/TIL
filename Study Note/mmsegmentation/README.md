# mmsegmentation 사용법

> https://github.com/open-mmlab/mmsegmentation/blob/master/docs/en/get_started.md#installation



## 시작하기

```bash
$ pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/{cu_version}/{torch_version}/index.html
```



* 내가 사용한 것

```bash
$ pip install torch==1.10.0+cu111 torchvision==0.11.0+cu111 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html

$ pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.10/index.html

$ git clone https://github.com/open-mmlab/mmsegmentation.git

$ cd mmsegmentation

$ pip install -e .
```

