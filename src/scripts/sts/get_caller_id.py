import os
import boto3
from dotenv import load_dotenv

load_dotenv()

boto3.client('sts', endpoint_url=os.getenv('ENDPOINT_URL')).get_caller_identity()