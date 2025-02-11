from rich.console import Console
from rich.markdown import Markdown
import yaml
from utils.cli_output import print_return_values
from scripts.s3_buckets.list_s3_buckets import list_s3_buckets
from scripts.s3_buckets.get_s3_buckets_names import get_s3_bucket_names
from scripts.s3_buckets.delete_s3 import delete_s3_buckets

console = Console()

with open("styles/rich_styles.yaml", "r") as file:
    styles = yaml.safe_load(file)

with open('utils/RICH_MARKDOWN_MENU.md') as readme:
    markdown = Markdown(readme.read())

console.print(markdown)

def main_menu():
      while (True):
        console.print('\n[bold]1. Listar Buckets do S3 📋')
        console.print('[bold]2. Deletar um Bucket S3 :wastebasket:')
        console.print('[bold]3. Sair :wave:')

        user_input = int(input())
        
        match user_input:
            case 1:
                print_return_values(get_s3_bucket_names())
                continue
            case 2:
                delete_s3_buckets()
                continue
            case 3:
                print('Saindo...')
                break 
            case _:
                print('Opção inválida.')
                continue

if __name__ == "__main__":
    main_menu()