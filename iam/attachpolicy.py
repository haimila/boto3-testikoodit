import boto3

def attachpolicy(policy,groupname):

    iam = boto3.client("iam")
    iam.attach_group_policy(PolicyArn=policy,GroupName=groupname)

attachpolicy("arn:aws:iam::821383200340:policy/mitjantesti-ec2","mitjan_testigrouppi")