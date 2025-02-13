from textual.app import App
from textual import on
from textual.widgets import Button
from src.scripts.s3_buckets.get_s3_buckets_names import get_s3_bucket_names
from ui.screens.home import HomeScreen
from ui.screens.s3_buckets_list import S3BucketsListScreen

class Infrapulse(App):
    CSS_PATH = 'resources/styles.tcss'
    BINDINGS = []

    def __init__(self):
        super().__init__()
        self.bucket_names = [] 

    async def on_mount(self) -> None:
        await self.push_screen(HomeScreen())

    @on(Button.Pressed, '#list-s3-btn')
    async def list_s3_buckets(self) -> None:
            self.notify('Listando Buckets do S3...', timeout=2.0)
        
            names = get_s3_bucket_names()
                
            if isinstance(names, list):
                self.bucket_names = names 
                await self.push_screen(S3BucketsListScreen(self.bucket_names))
            else:
                self.notify('Erro ao listar buckets', severity='error', timeout=3.0)

    @on(Button.Pressed, '#back-btn')
    async def navigate_back(self):
            await self.pop_screen()

    @on(Button.Pressed, '#exit-btn')
    def exit_the_app(self):
            self.exit()

if __name__ == "__main__":
    app = Infrapulse()
    app.run()