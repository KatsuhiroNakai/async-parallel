# async-parallel
同期/非同期および並列処理のサンプル

## docker環境構築
```
$ docker image build -t async-parallel .
$ docker container run -it -v $(pwd)/src:/app/src -v $(pwd)/requirements.txt:/app/requirements.txt -p 80:80 --name async-parallel --rm async-parallel
```