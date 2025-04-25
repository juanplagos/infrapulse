from scripts.s3.get_s3_buckets_names import get_s3_bucket_names
from typing import Callable
import yaml

with open('resources/ptbr.yaml', 'r') as f:
    ptbr = yaml.safe_load(f)

def reload_page(self, screen_name: Callable) -> None:
    self.push_screen(screen_name)
    self.notify(ptbr['notification']['reloading'], timeout=2.0)
    self.bucket_names = get_s3_bucket_names()

if __name__ == '__main__':
    reload_page()