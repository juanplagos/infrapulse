import os
from dotenv import load_dotenv
import boto3

load_dotenv()

def get_client(service_name: str):
    return boto3.client(service_name, endpoint_url=os.getenv('ENDPOINT_URL'))