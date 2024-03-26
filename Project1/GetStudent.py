import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('STUDENT')

def lambda_handler(event, context):
    studId = event['studId']
    resp = table.get_item(Key={
        "STUDENT_ID":studId
    })
    return resp['Item']