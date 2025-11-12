import os
import boto3
from dotenv import load_dotenv

load_dotenv()

aws_access_key = os.getenv("ACCESS_KEY")
aws_secret_key = os.getenv("SECRET_ACCESS_KEY")
bucket = os.getenv("bucket_name")

print(bucket)