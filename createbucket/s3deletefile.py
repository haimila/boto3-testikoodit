import boto3

def delete_file(bucket,filename):

    s3 = boto3.resource("s3")
    objekti = s3.Object(bucket,filename)
    objekti.delete()

delete_file("mitjabucket","testitiedosto")