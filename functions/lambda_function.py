import os
import json
import boto3

IS_DEBUG = bool(os.getenv('IS_DEBUG', '0'))


def lambda_handler(event, context):
    confs = get_config_on_s3()
    print('!!!!!!!!!! HELLO WORLD !!!!!!!!!!')
    debug_print(confs)


def get_config_on_s3():
    BUCKET_NAME = os.getenv('CONFIG_S3_BUCKET_NAME')
    OBJECT_PATH = os.getenv('CONFIG_S3_OBJECT_PATH')
    debug_print([BUCKET_NAME, OBJECT_PATH])

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET_NAME)
    obj = bucket.Object(OBJECT_PATH)
    response = obj.get()
    body = response['Body'].read()
    return json.loads(body.decode('utf-8'))


def debug_print(msg, prefix='!!!!!!!!! '):
    if not IS_DEBUG:
        return

    if isinstance(msg, list):
        print(prefix + json.dumps(msg))
    elif isinstance(msg, dict):
        print(prefix + json.dumps(msg))
    else:
        print(prefix + str(msg))
