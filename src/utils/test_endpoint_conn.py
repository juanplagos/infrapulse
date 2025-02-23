import os
import yaml
import requests
from dotenv import load_dotenv

with open('resources/ptbr.yaml', 'r') as f:
    ptbr = yaml.safe_load(f)

def check_conn(self) -> None:
    try:
        self.r = requests.head(os.getenv('ENDPOINT_URL'))
        
    except requests.ConnectionError:
        self.notify(ptbr['notification']['connection_error'], severity='error', timeout=5.0)

if __name__ == 'main':
    check_conn()