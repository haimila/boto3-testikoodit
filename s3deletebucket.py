import boto3

def delete_bucket(bucketname):

    s3 = boto3.resource("s3")

    bucket = s3.Bucket(bucketname)
    for key in bucket.objects.all():
        key.delete()
    bucket.delete()

delete_bucket("mitjabucket")