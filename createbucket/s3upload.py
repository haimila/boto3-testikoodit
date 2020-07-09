import boto3

def upload_file(filename,bucket,object_name=None):

    if object_name is None:
        object_name = filename

    s3 = boto3.client("s3")
    s3.upload_file(filename,bucket,object_name)

upload_file("C:\\Users\\Mitja\\PycharmProjects\\Boto3-projektit\\createbucket\\töttöriina.txt","mitjabucket")