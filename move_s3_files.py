import boto3
from boto3 import client

def lambda_handler(event, context):

    bucket='Enter-name-of-your-bucket'

    s3 = boto3.resource('s3')
    conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
    for file in conn.list_objects(Bucket=bucket)['Contents']:
        obj = file['Key']
        print('obj', obj)
        temp = obj.split('/')
        # print('#######', temp, len(temp))
        key = temp[0]
        print(key)
        if len(temp) == 1 and key.endswith('.txt'):
            # print('***************', key)
            copy_source = {
            'Bucket': bucket,
            'Key': key
            }
            s3.meta.client.copy(copy_source, bucket, 'queued/{}'.format(key))
            
            conn.delete_object(
                Bucket='Enter-name-of-your-bucket',
                Key=key   
            )