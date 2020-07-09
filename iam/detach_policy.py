import boto3

def detach(policy,group):

    iam = boto3.client("iam")
    iam.detach_group_policy(PolicyArn=policy,GroupName=group)

detach("arn:aws:iam::821383200340:policy/mitjantesti-ec2","mitjan_testigrouppi")