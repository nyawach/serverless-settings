# opencv-python

## What is this?

`opencv-python` on AWS Lambda

## How to use

```bash
$ cd serverless/opencv-python
$ npm i
# edit `provider.profile` to your AWS profile name
$ vi serverless.yml
$ sls deploy
```

POST API endpoint (`https://xxx.execute-api.ap-northeast-1.amazonaws.com/dev/opencv`) with this body.

```json
{
  "image": "base64 string in sample/img_base64.txt"
}
```

You will respond this response body.

```json
{
  "cv2": "4.1.1",
  "numpy": "1.17.4",
  "width": 280,
  "height": 280
}
```
