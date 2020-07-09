import boto3

def s3_download(bucketname,objectname,filename):
    s3 = boto3.client("s3")
    s3.download_file(bucketname,objectname,filename)

s3_download("mitjabucket","töttöröö.txt","töttöriina.txt")