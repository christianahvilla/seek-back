import boto3
import os
from dotenv import load_dotenv

load_dotenv()

environment = os.getenv('ENVIRONMENT', 'local')

print(environment)

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
        region_name=os.getenv('AWS_REGION', 'us-west-2'),                    
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', 'fakeKey'),         
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY', 'fakeSecret')
    )

print(dynamodb)

# Crear tabla de usuarios
user_table = dynamodb.create_table(
    TableName='Users',
    KeySchema=[
        {'AttributeName': 'PK', 'KeyType': 'HASH'},
        {'AttributeName': 'SK', 'KeyType': 'RANGE'}
    ],
    AttributeDefinitions=[
        {'AttributeName': 'PK', 'AttributeType': 'S'},
        {'AttributeName': 'SK', 'AttributeType': 'S'}
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Crear tabla de tareas
task_table = dynamodb.create_table(
    TableName='Tasks',
    KeySchema=[
        {'AttributeName': 'PK', 'KeyType': 'HASH'},
        {'AttributeName': 'SK', 'KeyType': 'RANGE'}
    ],
    AttributeDefinitions=[
        {'AttributeName': 'PK', 'AttributeType': 'S'},
        {'AttributeName': 'SK', 'AttributeType': 'S'}
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

user_table.wait_until_exists()
task_table.wait_until_exists()
print("Tables created successfully!")