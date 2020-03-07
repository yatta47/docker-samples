# これはなに

docker-composeでNginxを立ち上げるためのyamlファイル。ポートは8080で待ち受けている。

# 動作確認マシン

```
$ docker --version
Docker version 19.03.2, build 6a30dfc
$ docker-compose version
docker-compose version 1.25.0-rc2, build 661ac20e
docker-py version: 4.0.1
CPython version: 3.7.4
OpenSSL version: OpenSSL 1.1.0k  28 May 2019
```

# 使い方

```
$ git clone https://github.com/yatta47/docker-samples.git
$ cd nginx
$ docker-compose up
```

