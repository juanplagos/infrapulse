from scripts.s3_buckets.list_s3 import list_s3_buckets, print_s3_bucket_names
from scripts.s3_buckets.delete_s3 import delete_s3_buckets

def main():
    while (True):
        print('\n1. Listar Buckets do S3 | 2. Deletar um Bucket do S3 | 0. Sair')
        user_input = int(input())
        
        match user_input:
            case 1:
                print_s3_bucket_names()
                continue
            case 2:
                delete_s3_buckets()
                continue
            case 0:
                print('Saindo...')
                break 
            case _:
                print('Opção inválida.')
                continue

if __name__ == "__main__" :
    main()