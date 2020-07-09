import boto3

def create_bucket(bucket_name, region=None):

    if region is None:
        s3 = boto3.client("s3")
        s3.create_bucket(Bucket=bucket_name)

    else:
        s3 = boto3.client("s3", region_name=region)
        location = {'LocationConstraint': region}
        s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

create_bucket("mitjan-boto3-testi", region="ap-northeast-1")