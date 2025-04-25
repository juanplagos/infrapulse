from utils.aws_clients import get_client

ec2 = get_client('ec2')

def ec2_instances():
    """
    
    """
    ec2.describe_instances()

if __name__ == "__main__":
    ec2_instances()