from textual.app import ComposeResult
from textual.containers import Center
from textual.widgets import Footer, Header, Button
from textual.screen import Screen
import yaml

with open('resources/ptbr.yaml', 'r') as f:
    ptbr = yaml.safe_load(f)

class EC2Screen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Center(
            Button(ptbr['button']['ec2_instance_summary_menu_opt'], id='ec2-summary-menu-opt-btn'),
            Button(ptbr['button']['back'], id='back-btn')
        )
        yield Footer()