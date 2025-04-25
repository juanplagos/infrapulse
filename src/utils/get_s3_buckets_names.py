from dotenv import load_dotenv
from utils.aws_clients import get_client

load_dotenv()

s3 = get_client('s3')

def get_s3_bucket_names() -> list:
    buckets = s3.list_buckets().get('Buckets', [])
    return [bucket['Name'] for bucket in buckets]

if __name__ == "__main__":  
    get_s3_bucket_names() 