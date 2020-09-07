import boto3

bucket_name = 'test-loop-bucket'
client = boto3.client('s3')
def iterate_bucket_items(bucket):
    """
    Generator that iterates over all objects in a given s3 bucket

    See http://boto3.readthedocs.io/en/latest/reference/services/s3.html#S3.Client.list_objects_v2 
    for return data format
    :param bucket: name of s3 bucket
    :return: dict of metadata for an object
    """
    paginator = client.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket)
    for page in page_iterator:
        if page['KeyCount'] > 0:
            for item in page['Contents']:
                yield item['Key']


for key in iterate_bucket_items(bucket=bucket_name):
    print(key)
    client.put_object_acl(ACL='public-read', Bucket=bucket_name, Key=key)