import boto3

def del_user(userid):

    iam = boto3.client("iam")
    iam.delete_user(UserName=userid)

del_user("MitjanTesti")