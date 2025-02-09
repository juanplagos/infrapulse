import os
import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client('s3', endpoint_url=os.getenv('ENDPOINT_URL'))

def list_s3_buckets():
    response = s3.list_buckets()

    print('Buckets do S3 existentes:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')
    
list_s3_buckets()