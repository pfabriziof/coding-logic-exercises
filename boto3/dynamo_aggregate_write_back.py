"""DynamoDB: Aggregate and Write Back

A table orders has items with fields customer_id, amount (Decimal), and status.
Scan the table for all orders where status = "completed", calculate the total
amount per customer, and write the results into a new table customer_totals
with fields customer_id and total.
"""

import boto3
from botocore.exceptions import ClientError
import logging
from decimal import Decimal
from collections import defaultdict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def check_tables_creation():
    orders_table = dynamodb.Table('orders')
    totals_table = dynamodb.Table('customer_totals')
    try:
        orders_table.load()
        totals_table.load()
        logger.info("tables already exist.")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            logger.info("Tables doesn't exist, creating a new one...")

            orders_table = dynamodb.create_table(
                    TableName='orders',
                    KeySchema=[
                        {'AttributeName': 'customer_id', 'KeyType': 'HASH'},
                        {'AttributeName': 'order_id', 'KeyType': 'RANGE'}
                        ],
                    AttributeDefinitions=[
                        {'AttributeName': 'customer_id', 'AttributeType': 'S'},
                        {'AttributeName': 'order_id', 'AttributeType': 'S'}
                        ],
                    BillingMode='PAY_PER_REQUEST'
                    )
            totals_table = dynamodb.create_table(
                    TableName='customer_totals',
                    KeySchema=[{'AttributeName': 'customer_id', 'KeyType': 'HASH'}],
                    AttributeDefinitions=[{'AttributeName': 'customer_id', 'AttributeType': 'S'}],
                    BillingMode='PAY_PER_REQUEST'
                    )

            logger.info("Waiting for tables to become active...")
            orders_table.wait_until_exists()
            populate_mock_data(orders_table)
            totals_table.wait_until_exists()
        else:
            raise e

    return orders_table, totals_table

def populate_mock_data(orders_table):
    """Helper function to insert sample data for testing."""
    logger.info("Populating sample data into orders table...")
    mock_orders = [
        {'customer_id': 'cust_1', 'order_id': 'o1', 'amount': Decimal('150.50'), 'status': 'completed'},
        {'customer_id': 'cust_1', 'order_id': 'o2', 'amount': Decimal('50.00'), 'status': 'completed'},
        {'customer_id': 'cust_2', 'order_id': 'o3', 'amount': Decimal('99.99'), 'status': 'completed'},
        {'customer_id': 'cust_1', 'order_id': 'o4', 'amount': Decimal('200.00'), 'status': 'pending'},
        {'customer_id': 'cust_2', 'order_id': 'o5', 'amount': Decimal('10.00'), 'status': 'cancelled'},
    ]
    with orders_table.batch_writer() as batch:
        for order in mock_orders:
            batch.put_item(Item=order)

if __name__ == "__main__":
    totals = defaultdict(Decimal)
    orders_table, totals_table = check_tables_creation()
    response = orders_table.scan(
            FilterExpression=boto3.dynamodb.conditions.Attr('status').eq('completed')
            )
    logger.info(response)

    while True:
        for item in response.get('Items', []):
            totals[item['customer_id']] += item['amount']

        if 'LastEvaluatedKey' not in response:
            break

        # Go to the next page / key
        response = orders_table.scan(
                FilterExpression=boto3.dynamodb.conditions.Attr('status').eq('completed'),
                ExclusiveStartKey=response['LastEvaluatedKey']
                )

    logger.info(totals.items())
    with totals_table.batch_writer() as batch:
        for customer_id, total in totals.items():
            batch.put_item(Item={
                'customer_id': customer_id,
                'total': total
                })
            print(f'Written: {customer_id} -> {total}')

