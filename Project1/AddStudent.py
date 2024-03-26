#CODE FOR BOTH DYNAMODB AND S3
import json
import boto3
import time

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')
table = dynamodb.Table('STUDENT')

def lambda_handler(event, context):
    table.put_item(Item=event)
    bucket_name = 'mys3-demo2bucket'
    time_stamp= str(int(time.time()))
    file_name = time_stamp+'.json'
    json_data = event 
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(json_data)
    )
    
    return {"code":200, "message":"Student Added Successfull"}

# code for dynamodb
# import json
# import boto3
# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('STUDENT')
# def lambda_handler(event, context):
#     table.put_item(Item=event)
#     return {"code":200, "message":"Student Added Successfull"}