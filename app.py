from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Footer, Header, Button, Static

class Infrapulse(HorizontalGroup):
    
    def compose(self) -> ComposeResult:
        yield Button('Listar Buckets do S3 🗒️', id='list-s3-btn')
        yield Button('Deletar Bucket do S3 🗑️', id='delete-s3-btn')
        
class InfrapulseApp(App):
    CSS_PATH = 'resources/styles.tcss'
    BINDINGS = [
        ('d', 'change_background_theme', 'Changes background theme'),
    ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static('              📊 Gerenciador de Recursos da AWS - Selecione uma operação:')
        yield Footer()
        yield VerticalScroll(Infrapulse())

if __name__ == "__main__" :
    app = InfrapulseApp()
    app.run()