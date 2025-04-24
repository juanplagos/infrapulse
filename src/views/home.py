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
            Button(ptbr['button']['main_menu_s3_buckets_btn'], id='main-menu-s3-buckets-btn'),
            Button(ptbr['button']['main_menu_ec2_instances_btn'], id='main-menu-ec2-instances-btn'),
            Button(ptbr['button']['exit'], id='exit-btn')
        )
        yield Footer()