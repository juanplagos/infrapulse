from utils.aws_clients import get_client

ec2 = get_client('ec2')

def get_ec2_instance_info() -> list[dict]:
    try:
        instances_info = ec2.describe_instances()
        instances = []

        for reservation in instances_info['Reservations']:
            for instance in reservation['Instances']:
                instances.append({
                    'InstanceId': instance['InstanceId'],
                    'State': instance['State']['Name'],
                    'InstanceType': instance['InstanceType'],
                    'PublicIpAddress': instance.get('PublicIpAddress', 'Sem IP público'),
                    'PrivateIpAddress': instance.get('PrivateIpAddress', 'Sem IP privado'),
                    'LaunchTime': str(instance['LaunchTime']),
                    'AvailabilityZone': instance['Placement']['AvailabilityZone']
                })

        return instances

    except Exception as e:
        self.notify(f'Erro ao listar instâncias: {e}', severity='error', timeout=0.5)
        return []
