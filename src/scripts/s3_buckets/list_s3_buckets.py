from dotenv import load_dotenv
from utils.aws_clients import get_client

load_dotenv()

s3 = get_client('s3')

def list_s3_buckets() -> dict:
    """Retrieves a list of all S3 buckets available.

        Returns:
            dict: Contains:
            - Buckets (list): Each has Name (str), CreationDate (datetime), BucketRegion (str)
            - Owner (dict): Has DisplayName and ID
            - ContinuationToken (str): For pagination
            - Prefix (str): Bucket name filter
    """
    buckets_list = s3.list_buckets()
    return buckets_list

if __name__ == "__main__":  
    list_s3_buckets() 
