import os
import boto3
from dotenv import load_dotenv
from scripts.s3_buckets.list_s3_buckets import list_s3_buckets

load_dotenv()

s3 = boto3.client('s3', endpoint_url=os.getenv('ENDPOINT_URL'))

def delete_s3_buckets(self) -> None:
    self.users_bucket_name = self.query_one('#user_bucket_name').value
    
    self.notify(f'Deletando bucket {self.users_bucket_name}...', timeout=2.0)
    s3.delete_bucket(Bucket=self.users_bucket_name)
    self.notify(f'Bucket {self.users_bucket_name} deletado com sucesso.')

if __name__ == "__main__":
    delete_s3_buckets()  