""" The Resource Auditor

Write a Python script that identifies all files in a specific S3 bucket ('production-data') that have a .log extension and were modified in the year 2026. The script must handle large buckets efficiently and gracefully handle cases where the bucket does not exist or access is denied."""

import boto3
import botocore

SOURCE_BUCKET = 'boto3-practices-bucket'
PREFIX = 'logs/'

def audit_logs(target_year):
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_objects_v2')
    log_files = []

    try:
        page_iterator = paginator.paginate(Bucket=SOURCE_BUCKET, Prefix=PREFIX)
        for page in page_iterator:
            if 'Contents' not in page:
                continue

            for obj in page['Contents']:
                key = obj['Key']
                last_modified = obj['LastModified']

                if key.endswith('.log') and last_modified.year == target_year:
                    log_files.append({
                        'Key': key,
                        'Size': obj['Size'],
                        'LastModified': last_modified.isoformat()
                        })
        return log_files

    except botocore.exceptions.ClientError as e:
        msg = {f'Error while operating with the bucket: {e}'}
        return msg


if __name__ == "__main__":
    results = audit_logs(2026)
    print('Printing results')
    for item in results:
        # print(item)
        print(f"Match found: {item['Key']} ({item['Size']} bytes)")
