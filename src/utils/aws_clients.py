import os
from dotenv import load_dotenv
import boto3

load_dotenv()

def get_s3_client():
    return boto3.client('s3', endpoint_url=os.getenv('ENDPOINT_URL'))