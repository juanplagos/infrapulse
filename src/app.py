from textual import on
from textual.app import App
from textual.widgets import Button
from views.home import HomeScreen
from views.s3.main_s3 import S3Screen
from views.s3.list_s3_buckets import S3BucketsListScreen
from views.s3.delete_s3_buckets import S3BucketsDeleteScreen
from views.ec2.main_ec2 import EC2Screen
from views.ec2.ec2_summary import EC2InstanceScreen
from utils.validate_s3_buckets import validate_bucket_list
from utils.reload_page import reload_page
from utils.check_endpoint_conn import check_conn
from scripts.s3.delete_s3_buckets import delete_s3_buckets
import yaml

with open('resources/ptbr.yaml', 'r') as f:
    ptbr = yaml.safe_load(f)

class Infrapulse(App):
    CSS_PATH = 'resources/styles.tcss'
    BINDINGS = []

    def __init__(self):
        super().__init__()
        self.bucket_names = [] 

    def on_mount(self) -> None:
        check_conn(self)
        self.push_screen(HomeScreen())

    @on(Button.Pressed, '#main-menu-ec2-instances-btn')
    async def ec2_screen(self) -> None:
        self.push_screen(EC2Screen())

    @on(Button.Pressed, '#ec2-summary-menu-opt-btn')
    async def ec2_input_screen(self) -> None:
        self.push_screen(EC2InstanceScreen())
    
    @on(Button.Pressed, '#main-menu-s3-buckets-btn')
    async def s3_screen(self) -> None:
        self.push_screen(S3Screen())

    @on(Button.Pressed, '#list-s3-btn')
    async def list_s3_buckets(self) -> None:
        self.notify(ptbr['notification']['listing'], timeout=2.0)
        await validate_bucket_list(self, S3BucketsListScreen())

    @on(Button.Pressed, '#delete-s3-btn')
    async def delete_s3_buckets(self) -> None:
        await validate_bucket_list(self, S3BucketsDeleteScreen())
        
    @on(Button.Pressed, '#s3-screen-back-btn')
    async def navigate_back_s3_screen(self) -> None:
        self.push_screen(S3Screen())

    @on(Button.Pressed, '#ec2-screen-back-btn')
    async def navigate_back_ec2_screen(self) -> None:
        self.push_screen(EC2Screen())

    @on(Button.Pressed, '#back-btn')
    async def navigate_back_home_screen(self) -> None:
        self.push_screen(HomeScreen())
    
    @on(Button.Pressed, '#reload-list-btn')
    def refresh_list_page(self) -> None: 
        reload_page(self, S3BucketsListScreen())

    @on(Button.Pressed, '#reload-delete-list-btn')
    def refresh_delete_page(self) -> None:
        reload_page(self, S3BucketsDeleteScreen())

    @on(Button.Pressed, '#delete-bucket-btn')
    def delete_buckets(self) -> None:
        delete_s3_buckets(self)

    @on(Button.Pressed, '#exit-btn')
    def exit_the_app(self) -> None:
        self.exit()

if __name__ == '__main__':
    app = Infrapulse()
    app.run()