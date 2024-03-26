import json
import boto3

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employee')

def lambda_handler(event, context):
    # TODO implement
    bucket=event['Records'][0]['s3']['bucket']['name'] #fetch bucket name
    s3_file_name=event['Records'][0]['s3']['object']['key'] #fetch file name
    resp=s3_client.get_object(Bucket=bucket,Key=s3_file_name)
    data=resp['Body'].read().decode("utf-8")
    empl=data.split("\n")
    print(empl)
    
    for emp in empl:
        print(emp)
        empdata=emp.split(",")
        #put data in dynamodb
        try:
             table.put_item(
               Item={
                   "emp_id":empdata[0],
                    "LOCATION":empdata[1],
                    "STUDENT_NAME":empdata[2]
                   
               }
              )
        except Exception as e:
            print("End of line")
        
    
    return "hello from lambda"
    
