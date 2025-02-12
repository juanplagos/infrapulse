import os
import boto3
from dotenv import load_dotenv
from rich.prompt import Prompt
from scripts.s3_buckets.list_s3_buckets import list_s3_buckets

load_dotenv()

s3 = boto3.client('s3', endpoint_url=os.getenv('ENDPOINT_URL'))

def delete_s3_buckets() -> None:
    """Prompts the user for the name of a S3 Bucket. 
    If an existent bucket name is provided, deletes the bucket, 
    otherwise lets user know that the bucket does not exist.
    """
    user_bucket_name = Prompt.ask('[bold]Digite o nome do bucket do s3 que deseja deletar[bold]')

    buckets_list = list_s3_buckets()
    
    if user_bucket_name in [bucket['Name'] for bucket in buckets_list.get('Buckets', [])]:
        print(f'\nDeletando bucket {user_bucket_name}...')
        deleted_bucket = s3.delete_bucket(Bucket=user_bucket_name,)
        print(f'\nBucket {user_bucket_name} deletado com sucesso.')
    else:
        print('Este bucket não existe.')

if __name__ == "__main__":
    delete_s3_buckets()  