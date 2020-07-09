import json
import boto3
from botocore.exceptions import ClientError

def full_access(policyname,service):
    try:
        iam = boto3.client("iam")

        policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": f"{service}:*",
                "Resource": "*"
            }
        ]}

        response = iam.create_policy(
            PolicyName=policyname,
            PolicyDocument=json.dumps(policy)
        )
        print(response)
    except ClientError as e:
        print(e)
        return False
    return True

print(full_access("mitjantesti-ec2","ec2"))