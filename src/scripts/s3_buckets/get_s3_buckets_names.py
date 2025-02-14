import os
import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client('s3', endpoint_url=os.getenv('ENDPOINT_URL'))

def get_s3_bucket_names() -> list:
    buckets_list = s3.list_buckets()
    no_buckets = ['Não há buckets do S3 para listar.']
    bucket_names = [] 

    if not buckets_list['Buckets']:
        return no_buckets
    else:  
        for bucket in buckets_list['Buckets']:
            bucket_names.append(bucket["Name"])
    return bucket_names

if __name__ == "__main__":  
    get_s3_bucket_names() 