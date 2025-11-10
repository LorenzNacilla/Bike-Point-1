import os
import boto3
from dotenv import load_dotenv

load_dotenv()

aws_access_key = os.getenv("ACCESS_KEY")
aws_secret_key = os.getenv("SECRET_ACCESS_KEY")
bucket = os.getenv("bucket_name")

# print(bucket)

s3_client = boto3.client(
    "s3"
    , aws_access_key_id = aws_access_key
    , aws_secret_access_key = aws_secret_key
)

try:
    try:
        s3_client.list_buckets(bucket=bucket)
    except:
        print('Access Denied')
        sys.exit(1)
    
    dir = 'data'
    file = [f for f in os.listdir(dir) if f.endswith('.json')]
    if len(file) > 0:
        filename = dir + '/' + file[0]
        s3filename = file[0]
        s3_client.upload_file(filename, bucket, s3filename)
        os.remove(filename)
    else:
        print('No files to upload')
except Exception as e:
    print(e)
    raise


