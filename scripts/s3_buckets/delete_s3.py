import os
import boto3
from dotenv import load_dotenv
from scripts.s3_buckets.list_s3 import list_s3_buckets

load_dotenv()

s3 = boto3.client('s3', endpoint_url=os.getenv('ENDPOINT_URL'))

def delete_s3_buckets():
    user_bucket_name = input("Digite o nome do bucket do S3 a ser deletado: ")

    buckets_list = list_s3_buckets()
    
    if user_bucket_name in [bucket['Name'] for bucket in buckets_list.get('Buckets', [])]:
        print(f'\nDeletando bucket {user_bucket_name}...')
        deleted_bucket = s3.delete_bucket(Bucket=user_bucket_name,)
        print(f'\nBucket {user_bucket_name} deletado com sucesso.')
    else:
        print('Este bucket não existe.')