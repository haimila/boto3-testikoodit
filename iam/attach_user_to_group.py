import boto3

def add_user(userid,groupid):

    iam = boto3.client("iam")
    iam.add_user_to_group(UserName=userid,GroupName=groupid)

add_user("MitjanTesti","mitjan_testigrouppi")