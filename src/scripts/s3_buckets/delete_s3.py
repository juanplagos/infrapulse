import os
import boto3
from dotenv import load_dotenv
from rich.prompt import Prompt
from src.scripts.s3_buckets.list_s3_buckets import list_s3_buckets

load_dotenv()

s3 = boto3.client('s3', endpoint_url=os.getenv('ENDPOINT_URL'))

def delete_s3_buckets(self) -> None:
    """Prompts the user for the name of a S3 Bucket. 
    If an existent bucket name is provided, deletes the bucket, 
    otherwise lets user know that the bucket does not exist.
    """
    self.user_bucket_name = Prompt.ask('[bold]Digite o nome do bucket do s3 que deseja deletar')

    buckets_list = list_s3_buckets()
    
    if self.user_bucket_name in [bucket['Name'] for bucket in buckets_list.get('Buckets', [])]:
        self.notify(f'\nDeletando bucket {self.user_bucket_name}...')
        deleted_bucket = s3.delete_bucket(Bucket=self.user_bucket_name,)
        self.notify(f'\nBucket {self.user_bucket_name} deletado com sucesso.')
    else:
        print('Este bucket não existe.')

if __name__ == "__main__":
    delete_s3_buckets()  