import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url='http://localhost:8000',
    region_name='us-west-2',
    aws_access_key_id='fakeKey',
    aws_secret_access_key='fakeSecret'
)

user_table = dynamodb.Table('Users')

def create_user(email, name, password):
    user_table.put_item(
        Item={
            'PK': f'USER#{email}',
            'SK': 'PROFILE',
            'email': email,
            'name': name,
            'password': password
        },
        ConditionExpression='attribute_not_exists(PK)'
    )

def get_user(email):
    response = user_table.get_item(
        Key={
            'PK': f'USER#{email}',
            'SK': 'PROFILE'
        }
    )
    return response.get('Item')