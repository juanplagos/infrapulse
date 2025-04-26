from textual.app import ComposeResult
from textual.containers import Center
from textual.widgets import Header, Button, DataTable
from textual.screen import Screen
from scripts.ec2.get_ec2_instance_summary import get_ec2_instance_info
import yaml

with open('resources/ptbr.yaml', 'r') as f:
    ptbr = yaml.safe_load(f)

class EC2InstanceScreen(Screen):
    def compose(self) -> ComposeResult:
        instancias = get_ec2_instance_info()
        
        tabela = DataTable()
        tabela.add_columns(
            'ID da Instância', 
            'Estado', 
            'Tipo', 
            'IP Público', 
            'IP Privado', 
            'Data de Criação', 
            'Zona de Disponibilidade'
        )

        for instancia in instancias:
            tabela.add_row(
                instancia['InstanceId'],
                instancia['State'],
                instancia['InstanceType'],
                instancia['PublicIpAddress'],
                instancia['PrivateIpAddress'],
                instancia['LaunchTime'],
                instancia['AvailabilityZone']
            )

        yield Header('Resumo das Instâncias EC2')
        with Center():
            yield tabela
        
        with Center():
            yield Button(ptbr['button']['reload'], id='reload-btn')
            yield Button(ptbr['button']['back'], id='back-btn')