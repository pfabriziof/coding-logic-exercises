"""S3 + SQS: Event-Driven Pipeline

Files are uploaded to bucket boto-practices-bucket. For every .csv file found,
send a message to the SQS queue file-processing-queue containing the bucket name and key.
Then consume the queue and print a processing confirmation for each message.
"""
import json
from sys import prefix
import boto3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

session = boto3.Session(region_name='us-east-1')
s3 = session.client('s3')
sqs = session.client('sqs')

BUCKET = 'boto3-practices-bucket'
PREFIX = 'incoming-csv/'
QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/975050261044/file-processing-queue'

paginator = s3.get_paginator('list_objects_v2')
pages = paginator.paginate(Bucket=BUCKET, Prefix=PREFIX)

for page in pages:
    for obj in page.get('Contents', []):
        key = obj['Key']
        if key.endswith('.csv'):
            message = json.dumps({'bucket': BUCKET, 'key': 'key'})
            sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=message)
            logger.info(f'Enqueued: {key}')

while True:
    response = sqs.receive_message(
            QueueUrl=QUEUE_URL,
            MaxNumberOfMessages=10,
            WaitTimeSeconds=5
            )

    messages = response.get('Messages', [])
    if not messages:
        print('Queue empty, done.')
        break

    for msg in messages:
        body = json.loads(msg['Body'])
        logger.info(f"Processsing: s3://{body['bucket']}/{body['key']}")

        sqs.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=msg['ReceiptHandle']
        )

