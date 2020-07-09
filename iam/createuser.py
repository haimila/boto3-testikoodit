import boto3

def create_user(name):

    iam = boto3.client("iam")
    iam.create_user(UserName=name)

create_user("MitjanTesti")