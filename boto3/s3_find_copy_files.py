"""S3: Find and Copy Stale Files

You have a bucket boto3-practices-bucket. Any file under the prefix reports/
that is larger than 1MB and hasn't been modified in over 30 days must be copied
to a bucket called cold-storage and then deleted from the original.
"""

import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')

SOURCE_BUCKET = 'boto3-practices-bucket'
DEST_BUCKET = 'boto3-practices-cold'
PREFIX = 'reports/'
SIZE_THRESHOLD = 1 * 1024 * 1024 # 1MB
DAYS_THRESHOLD = 30

cutoff = datetime.now(timezone.utc) - timedelta(days=DAYS_THRESHOLD)

paginator = s3.get_paginator('list_objects_v2')
pages = paginator.paginate(Bucket=SOURCE_BUCKET, Prefix=PREFIX)

for page in pages:
    for obj in page.get('Contents', []):
        key = obj['Key']
        size = obj['Size']
        last_modified = obj['LastModified']

        # if size > SIZE_THRESHOLD and last_modified < cutoff:
        if key.endswith('.txt'):
            s3.copy_object(
                    CopySource = {'Bucket': SOURCE_BUCKET, 'Key': key},
                    Bucket=DEST_BUCKET,
                    Key=key
                    )
            s3.delete_object(Bucket=SOURCE_BUCKET, Key=key)
            print(f"Archided: {key}")
