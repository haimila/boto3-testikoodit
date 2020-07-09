import boto3

def list_buckets():

    s3 = boto3.client("s3")

    vastaus_json = s3.list_buckets()

    for bucket in vastaus_json["Buckets"]:
        print(f"{bucket['Name']}")

list_buckets()