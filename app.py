from textual.app import App, ComposeResult
from textual.containers import Center
from textual.widgets import Footer, Header, Button, Static
from textual.screen import Screen
from scripts.s3_buckets.get_s3_buckets_names import get_s3_bucket_names
from scripts.s3_buckets.delete_s3 import delete_s3_buckets

class HomeScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static('📊 Gerenciador de Recursos da AWS - Selecione uma operação:')
        yield Footer()
        yield Center(
            Button('Listar Buckets do S3 🗒️', id='list-s3-btn',),
            Button('Deletar Bucket do S3 🗑️', id='delete-s3-btn',),
            Button('Sair', id='exit-btn',)
        )

class S3BucketsListScreen(Screen):
    def __init__(self, names_display: Static):
        super().__init__()
        self.names_display = names_display  

    def compose(self) -> ComposeResult:
        yield Center(
            self.names_display,  
            Button('Back', id='back-btn')
        )

class InfrapulseApp(App):
    CSS_PATH = 'resources/styles.tcss'
    BINDINGS = []

    def __init__(self):
        super().__init__()
        self.names_display = Static("", id='s3-buckets-list')  

    async def on_mount(self) -> None:
        await self.push_screen(HomeScreen())

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'list-s3-btn':
            await self.push_screen(S3BucketsListScreen(self.names_display))
            names = get_s3_bucket_names()
            
            if isinstance(names, str):
                self.names_display.update(names)
            else:
                self.names_display.update('\n'.join(names)) 

        elif event.button.id == 'delete-s3-btn':
            pass

        elif event.button.id == 'back-btn':
            await self.pop_screen()

        elif event.button.id == 'exit-btn':
            self.exit()

if __name__ == "__main__":
    app = InfrapulseApp()
    app.run()