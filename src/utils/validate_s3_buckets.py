from scripts.s3.get_s3_buckets_names import get_s3_bucket_names
import yaml
from typing import Callable

with open('resources/ptbr.yaml', 'r') as f:
    ptbr = yaml.safe_load(f)

async def validate_bucket_list(self, screen_name: Callable) -> None:
    names = get_s3_bucket_names()

    if names or names == []:
        self.push_screen(screen_name)
    else:
        self.notify(ptbr['notification']['error_listing_buckets'], severity='error', timeout=3.0)
        self.push_screen(screen_name)

if __name__ == '__main__':
    validate_bucket_list()