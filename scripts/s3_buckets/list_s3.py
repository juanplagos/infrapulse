import os
import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client('s3', endpoint_url=os.getenv('ENDPOINT_URL'))

def list_s3_buckets():
    buckets_list = s3.list_buckets()
    
    if not buckets_list['Buckets']:
        print('Não há buckets do S3 para listar.')
    else:    
        print('\nBuckets do S3 existentes:')
        for bucket in buckets_list['Buckets']:
            print(f'  Nome: {bucket["Name"]}')
    return buckets_list