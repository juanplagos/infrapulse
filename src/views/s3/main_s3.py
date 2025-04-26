from textual.app import ComposeResult
from textual.containers import Center
from textual.widgets import Footer, Header, Button
from textual.screen import Screen
import yaml

with open('resources/ptbr.yaml', 'r') as f:
    ptbr = yaml.safe_load(f)

class S3Screen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Center(
            Button(ptbr['button']['list_buckets_menu_opt'], id='list-s3-btn'),
            Button(ptbr['button']['delete_buckets_menu_opt'], id='delete-s3-btn'),
            Button(ptbr['button']['back'], id='back-btn')
        )
        yield Footer()