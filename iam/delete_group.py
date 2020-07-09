import boto3

def del_group(group):

    iam = boto3.client("iam")

    iam.delete_group(GroupName=group)

del_group("mitjan_testigrouppi")