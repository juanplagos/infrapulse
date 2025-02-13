from textual import on
from textual.app import App
from textual.widgets import Button
from ui.screens.home import HomeScreen
from ui.screens.s3_buckets_list import S3BucketsListScreen
from ui.screens.delete_s3_buckets import S3BucketsDeleteScreen
from utils.validate_s3_buckets_list import list_check
from utils.reload_page import reload_page
import yaml

with open("resources/ptbr.yaml", "r") as f:
    ptbr = yaml.safe_load(f)

class Infrapulse(App):
    CSS_PATH = 'resources/styles.tcss'
    BINDINGS = []

    def __init__(self):
        super().__init__()
        self.bucket_names = [] 

    def on_mount(self) -> None:
        self.push_screen(HomeScreen())

    @on(Button.Pressed, '#list-s3-btn')
    async def list_s3_buckets(self) -> None:
        self.notify(ptbr['notification']['listing'], timeout=2.0)
        await list_check(self, S3BucketsListScreen(self.bucket_names))

    @on(Button.Pressed, '#delete-s3-btn')
    async def delete_s3_buckets(self) -> None:
        await list_check(self, S3BucketsDeleteScreen(self.bucket_names))

    @on(Button.Pressed, '#back-btn')
    async def navigate_back(self) -> None:
        self.pop_screen()
    
    @on(Button.Pressed, '#reload-btn')
    def refresh_page(self) -> None:
        reload_page(self)

    @on(Button.Pressed, '#exit-btn')
    def exit_the_app(self) -> None:
        self.exit()

if __name__ == "__main__":
    app = Infrapulse()
    app.run()