from textual.app import ComposeResult
from textual.containers import Center
from textual.widgets import Footer, Header, Button, Static
from textual.screen import Screen
import yaml

with open('resources/ptbr.yaml', 'r') as f:
    ptbr = yaml.safe_load(f)

class HomeScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static(ptbr['static']['main_header'], id='main-header')
        yield Center(
            Button(ptbr['button']['list_buckets'], id='list-s3-btn'),
            Button(ptbr['button']['delete_bucket'], id='delete-s3-btn'),
            Button(ptbr['button']['exit'], id='exit-btn')
        )
        yield Footer()