import boto3
from boto3.dynamodb.conditions import Key
import os
from dotenv import load_dotenv

load_dotenv()

environment = os.getenv('ENVIRONMENT', 'local')

if environment == 'local':
    dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url=os.getenv('DYNAMODB_ENDPOINT', 'http://localhost:8000'),
        region_name=os.getenv('AWS_REGION', 'us-west-2'),                    
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', 'fakeKey'),         
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY', 'fakeSecret')
    )
else:
    dynamodb = boto3.resource(
        'dynamodb',
        region_name=os.getenv('AWS_REGION', 'us-west-2')
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

def delete_user(email):
    user_table.delete_item(
        Key={
            'PK': f'USER#{email}',
            'SK': 'PROFILE'
        }
    )