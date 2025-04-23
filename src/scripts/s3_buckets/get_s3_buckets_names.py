import os
import boto3
from dotenv import load_dotenv
from utils.aws_clients import get_s3_client

load_dotenv()

s3 = get_s3_client()

def get_s3_bucket_names() -> list:
    buckets_list = s3.list_buckets()
    no_buckets = []
    bucket_names = [] 

    if not buckets_list['Buckets']:
        return no_buckets
    else:  
        for bucket in buckets_list['Buckets']:
            bucket_names.append(bucket["Name"])
    return bucket_names

if __name__ == "__main__":  
    get_s3_bucket_names() 