from textual.app import ComposeResult
from textual.containers import Center
from textual.widgets import Header, Button, Static
from textual.screen import Screen
from scripts.s3.get_s3_buckets_names import get_s3_bucket_names
import yaml

with open('resources/ptbr.yaml', 'r') as f:
    ptbr = yaml.safe_load(f)

class S3BucketsListScreen(Screen):
    def _init_(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        self.bucket_names = get_s3_bucket_names()

        yield Header()
        with Center():
            if not self.bucket_names:
                 
                 yield Static(ptbr['static']['no_buckets'])
                 with Center():
                    yield Button(ptbr['button']['reload_list'], id='reload-list-btn')
                    yield Button(ptbr['button']['back'], id='s3-screen-back-btn')
            else: 
                for bucket in self.bucket_names:
                    yield Static(f'{bucket}')
                with Center():
                    yield Button(ptbr['button']['reload_list'], id='reload-list-btn')
                    yield Button(ptbr['button']['back'], id='s3-screen-back-btn')