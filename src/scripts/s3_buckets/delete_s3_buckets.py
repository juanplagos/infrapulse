import os
import boto3
from dotenv import load_dotenv
from scripts.s3_buckets.list_s3_buckets import list_s3_buckets
from utils.aws_clients import get_s3_client

load_dotenv()

s3 = get_s3_client()

# Deletes empty s3 buckets
def delete_s3_buckets(self) -> None:
    self.users_bucket_name = self.query_one('#user_bucket_name').value
    
    self.notify(f'Deletando bucket {self.users_bucket_name}...', timeout=2.0)

    try:
        s3.delete_bucket(Bucket=self.users_bucket_name)
        self.notify(f'Bucket {self.users_bucket_name} deletado com sucesso.')
    except Exception as e:
        self.notify(f'Erro ao deletar bucket: {e}', severity='error', timeout=5.0)

if __name__ == "__main__":
    delete_s3_buckets()  