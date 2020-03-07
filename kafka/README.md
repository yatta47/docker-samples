# これはなに

kafka, zookeeperを動かすdocker-composeファイル

# 事前準備
## インストール

Dokcerおよびdocker-composeがインストールされていること

## コンフィグ編集
KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://192.168.33.72:9092

のIP部分（上記だと`192.168.33.72`部分）を環境に合わせて変更する。

# 使い方

```
$ cd kafka
$ docker-compose up
```
