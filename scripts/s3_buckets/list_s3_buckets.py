import os
import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client('s3', endpoint_url=os.getenv('ENDPOINT_URL'))

def list_s3_buckets() -> dict:
    """Retrieves a list of all S3 buckets available.

    :return: 
        dict: a dictionary containing bucket details (Name, CreationDate, etc.)
    """
    buckets_list = s3.list_buckets()
    return buckets_list

if __name__ == "__main__":  
    list_s3_buckets() 
