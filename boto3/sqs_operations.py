""" A Sample Tutorial

This tutorial will show you how to use Boto3 with an AWS service. In this sample tutorial, you will learn how to use Boto3 with Amazon Simple Queue Service (SQS).
"""
import boto3
import botocore
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

sqs = boto3.resource('sqs', region_name='us-east-1')
try:
    logger.info('Retrieving existing queue...')
    queue = sqs.get_queue_by_name(QueueName='test')
except botocore.exceptions.ClientError as e:
    logger.error('Queue doesn\'t exist, creating a new one')
    queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})


print(queue.url)
print(queue.attributes.get('DelaySeconds'))

for queue in sqs.queues.all():
    print(queue.url)

logger.info('Sending a message to the end of the queue...')
response = queue.send_message(MessageBody='world')

print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))

logger.info('Creating a message with custom attributes...')
response = queue.send_message(MessageBody='boto3', MessageAttributes={
    'Author': {
        'StringValue': 'Daniel',
        'DataType': 'String'
        }
    })
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))

logger.info('Sending messages in batches...')
response = queue.send_messages(Entries=[
    {
        'Id': '1',
        'MessageBody': 'world'
    },
    {
        'Id': '2',
        'MessageBody': 'boto3',
        'MessageAttributes': {
            'Author': {
                'StringValue': 'Daniel',
                'DataType': 'String'
            }
        }
    }
])

print(response.get('Failed'))

logger.info('Processing messages')
for message in queue.receive_messages(MessageAttributeNames=['Author']):
    author_text = ''
    if message.message_attributes is not None:
        author_name = message.message_attributes.get('Author').get('StringValue')
        if author_name:
            author_text = f'({author_name})'

    print(f'Hello, {message.body}! {author_text}')
    message.delete()

