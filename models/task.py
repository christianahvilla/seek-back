import boto3

dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url='http://localhost:8000',
    region_name='us-west-2',
    aws_access_key_id='fakeKey',
    aws_secret_access_key='fakeSecret'
)

table = dynamodb.Table('Tasks')

def create_task(task_id, title, description, status):
    table.put_item(
        Item={
            'PK': f'TASK#{task_id}',
            'SK': 'DETAILS',
            'title': title,
            'description': description,
            'status': status
        }
    )

def get_tasks():
    response = table.scan()
    return response['Items']

def get_task(task_id):
    response = table.get_item(
        Key={
            'PK': f'TASK#{task_id}',
            'SK': 'DETAILS'
        }
    )
    return response.get('Item')

def update_task(task_id, title=None, description=None, status=None):
    update_expression = []
    expression_values = {}
    expression_names = {}

    if title:
        update_expression.append("title = :title")
        expression_values[':title'] = title
    if description:
        update_expression.append("description = :description")
        expression_values[':description'] = description
    if status:
        update_expression.append("#status = :status")
        expression_values[':status'] = status
        expression_names['#status'] = 'status'

    table.update_item(
        Key={
            'PK': f'TASK#{task_id}',
            'SK': 'DETAILS'
        },
        UpdateExpression="SET " + ", ".join(update_expression),
        ExpressionAttributeValues=expression_values,
        ExpressionAttributeNames=expression_names
    )

def delete_task(task_id):
    table.delete_item(
        Key={
            'PK': f'TASK#{task_id}',
            'SK': 'DETAILS'
        }
    )