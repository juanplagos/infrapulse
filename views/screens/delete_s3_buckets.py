from textual.app import ComposeResult
from textual.containers import Center
from textual.widgets import Header, Button, Static
from textual.screen import Screen
from src.scripts.s3_buckets.get_s3_buckets_names import get_s3_bucket_names
import yaml

with open("resources/ptbr.yaml", "r") as f:
    ptbr = yaml.safe_load(f)

class S3BucketsDeleteScreen(Screen):
    def __init__(self, bucket_names: list):
        super().__init__()
        self.bucket_names = get_s3_bucket_names()
        
    def compose(self) -> ComposeResult:
            yield Header()
            with Center():
                if not self.bucket_names:
                     yield Static(ptbr['static']['no_buckets'])
                     yield Button(ptbr['button']['back'], id='back-btn')
                     yield Button(ptbr['button']['reload_list'], id='reload-list-btn')
                else:     
                    for index, bucket in enumerate(self.bucket_names):
                        delete_buckets_button_id = f'button-{index}-{bucket}'
                        yield Button(f'{bucket}', id=delete_buckets_button_id, classes='delete-buckets-button')
                    with Center():
                        yield Button(ptbr['button']['back'], id='back-btn')
                        yield Button(ptbr['button']['reload_delete_list'], id='reload-delete-list-btn')