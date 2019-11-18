# opencv-python

## What is this?

`opencv-python` をLambda で利用するための環境です。

- `serverless-python-requirementspython` で Lambda Layer にパッケージをまとめてアップロード
  + パッケージをDocker環境（`lambci/lambda:build-python3.7` イメージ）でインストール+zip
- 最初から次のパッケージが入っています
  + `python-opencv`
  + `numpy`
  + `boto3`
- Lambda Layer の容量制限（展開ファイルが250MBまで）にひっかかるので、これに FlaskなどのAPIを組み込むのは厳しいです。  
  OpenCV使う専用の Lambda として運用するのが良いと思います。


## How to use

1. `provider.profile` を `~/.aws/credentials` に書いた案件のプロファイルに変更してください。
2. メイン関数の memorySize / timeout については好みで設定を変更してください  
  初期設定でMAX設定にしています。
3. Docker を起動してください。
4. `cd serverless/opencv-python`
5. `npm i`
6. `sls deploy`
7. `sample/img_base64.txt` を↓リクエストボディにしてPOSTしてみる  
  ```json
  {
    "image": "<sample/img_base64.txtの中身>"
  }
  ```
8. ↓レスポンスが帰ってくればOK  
  ```json
  {
    "cv2": "4.1.1",
    "numpy": "1.17.4",
    "width": 280,
    "height": 280
  }
  ```
