from textual.app import ComposeResult
from textual.containers import Center, Container
from textual.widgets import Header, Button, Static, Input
from textual.screen import Screen
from scripts.s3.get_s3_buckets_names import get_s3_bucket_names
import yaml

with open('resources/ptbr.yaml', 'r') as f:
    ptbr = yaml.safe_load(f)

class S3BucketsDeleteScreen(Screen):
    def _init_(self):
        super().__init__()
        
    def compose(self) -> ComposeResult:
        self.bucket_names = get_s3_bucket_names()

        yield Header()
        with Center():
            if not self.bucket_names:
                 yield Static(ptbr['static']['no_buckets'])
                 with Center():
                    yield Button(ptbr['button']['reload_list'], id='reload-delete-list-btn')
                    yield Button(ptbr['button']['back'], id='s3-screen-back-btn')
            else:     
                with Container(id='s3-buckets-static-container'):
                            with Center():
                                for index, bucket in enumerate(self.bucket_names):
                                    static_id = f'button_{index}'
                                    yield Static(f'{bucket}', id=static_id, classes='s3-buckets-static-buttons')
                with Center():
                    yield Input(placeholder=ptbr['input']['delete_buckets_prompt'], id='user_bucket_name')
                    with Center():
                        yield Button(ptbr['button']['delete_bucket'], id='delete-bucket-btn')
                        yield Button(ptbr['button']['reload_list'], id='reload-delete-list-btn')
                        yield Button(ptbr['button']['back'], id='s3-screen-back-btn')