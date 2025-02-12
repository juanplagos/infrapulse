from textual.app import App, ComposeResult
from textual.containers import Center, Vertical
from textual.widgets import Footer, Header, Button, Static
from textual.screen import Screen
from scripts.s3_buckets.get_s3_buckets_names import get_s3_bucket_names
from scripts.s3_buckets.delete_s3 import delete_s3_buckets
import yaml

with open("resources/ptbr.yaml", "r") as f:
    ptbr = yaml.safe_load(f)

class HomeScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static(ptbr['static']['main_header'])
        yield Footer()
        yield Center(
            Button(ptbr['button']['list_buckets'], id="list-s3-btn"),
            Button(ptbr['button']['delete_bucket'], id='delete-s3-btn'),
            Button(ptbr['button']['exit'], id='exit-btn')
        )

class S3BucketsListScreen(Screen):
    def __init__(self, bucket_names: list):
        super().__init__()
        self.bucket_names = bucket_names

    def compose(self) -> ComposeResult:
            yield Header()
            with Vertical():
                for bucket in self.bucket_names:
                    yield Static(f'Nome: {bucket}')
                yield Button(ptbr['button']['back'], id='back-btn')

class Infrapulse(App):
    CSS_PATH = 'resources/styles.tcss'
    BINDINGS = []

    def __init__(self):
        super().__init__()
        self.bucket_names = [] 

    async def on_mount(self) -> None:
        await self.push_screen(HomeScreen())

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'list-s3-btn':
            self.notify('Listando Buckets do S3...', timeout=2.0)
        
            names = get_s3_bucket_names()
            
            if isinstance(names, list):
                self.bucket_names = names 
                await self.push_screen(S3BucketsListScreen(self.bucket_names))
            else:
                self.notify('Erro ao listar buckets', severity='error', timeout=3.0)

        elif event.button.id == 'back-btn':
            await self.pop_screen()

        elif event.button.id == 'delete-s3-btn':
            pass

        elif event.button.id == 'exit-btn':
            self.exit()

if __name__ == "__main__":
    app = Infrapulse()
    app.run()