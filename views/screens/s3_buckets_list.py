from textual.app import ComposeResult
from textual.containers import Center
from textual.widgets import Header, Button, Static
from textual.screen import Screen
import yaml

with open("resources/ptbr.yaml", "r") as f:
    ptbr = yaml.safe_load(f)

class S3BucketsListScreen(Screen):
    def __init__(self, bucket_names: list):
        super().__init__()
        self.bucket_names = bucket_names

    def compose(self) -> ComposeResult:
            yield Header()
            with Center():
                for bucket in self.bucket_names:
                    yield Static(f'{bucket}')
                yield Button(ptbr['button']['back'], id='back-btn')
                yield Button(ptbr['button']['reload'], id='reload-btn')