import os
import requests
from dotenv import load_dotenv

def check_conn(self) -> None:
    try:
        self.r = requests.head(os.getenv('ENDPOINT_URL'))
        
    except requests.ConnectionError:
        self.notify(f'Não foi possível conectar ao serviço da AWS. Verifique sua conexão de rede ou tente novamente mais tarde.', severity='error', timeout=5.0)