import json
import cv2
import numpy as np
import base64
from logging import getLogger

logger = getLogger(__name__)

def base64_to_img(img_base64: str):
    """Base64形式の文字列をOpenCVで利用できる画像バイナリに変換する
    """
    img_binary = base64.urlsafe_b64decode(img_base64)
    png = np.frombuffer(img_binary, dtype=np.uint8)
    img = cv2.imdecode(png, cv2.IMREAD_ANYCOLOR)
    return img

def handler(event, context):
    body = json.loads(event['body'])
    img_base64 = body.get('image')

    if img_base64 is None:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'image is required.'
            }, ensure_ascii=False)
        }

    img = base64_to_img(img_base64)
    h, w, _ = img.shape

    results = {
        'cv2': cv2.__version__,
        'numpy': np.__version__,
        'width': w,
        'height': h
    }
    logger.debug(event)
    return {
        'headers': {},
        'statusCode': 200,
        'body': json.dumps(results, ensure_ascii=False)
    }

if __name__ == "__main__":
    pass
