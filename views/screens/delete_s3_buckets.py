from textual.app import ComposeResult
from textual.containers import Center, Container
from textual.widgets import Header, Button, Static
from textual.screen import Screen
from src.scripts.s3_buckets.get_s3_buckets_names import get_s3_bucket_names
import yaml

with open("resources/ptbr.yaml", "r") as f:
    ptbr = yaml.safe_load(f)

class S3BucketsDeleteScreen(Screen):
    def _init_(self):
        super()._init_()
        
    def compose(self) -> ComposeResult:
        self.bucket_names = get_s3_bucket_names()

        yield Header()
        with Center():
            if not self.bucket_names:
                 yield Static(ptbr['static']['no_buckets'])
                 with Center():
                    yield Button(ptbr['button']['back'], id='back-btn')
                    yield Button(ptbr['button']['reload_delete_list'], id='reload-delete-list-btn')
            else:     
                with Container(id='s3-buckets-buttons-container'):
                            with Center():
                                for index, bucket in enumerate(self.bucket_names):
                                    button_id = f"button_{index}_{bucket}"
                                    yield Button(f'{bucket}', id=button_id, classes='s3-buckets-delete-buttons')
                with Center():
                    yield Button(ptbr['button']['back'], id='back-btn')
                    yield Button(ptbr['button']['reload_delete_list'], id='reload-delete-list-btn')