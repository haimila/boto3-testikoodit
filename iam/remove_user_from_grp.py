import boto3

def remove_user(group,user):

    iam = boto3.client("iam")
    iam.remove_user_from_group(GroupName=group, UserName=user)

remove_user("mitjan_testigrouppi","MitjanTesti")