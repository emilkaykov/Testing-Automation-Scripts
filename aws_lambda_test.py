import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor-count-table')

def lambda_handler(event, context):
response = table.get_item(Key= {'user' : 'views'} )
count = response["Item"]["views"]

new_view = str(int(count)+1)

response = table.put_item(Item={
    'user':'0',
    'views': new_view
})

return new_view


