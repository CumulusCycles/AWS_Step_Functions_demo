import json
import random

status_codes = ["200", "403", "500"]

def lambda_handler(event, context):
    print(event)
    
    status_code = random.choice(status_codes)

    if status_code == "500":
        raise Exception("InternalServerError")

    return {
        'statusCode': status_code,
        'body': json.dumps('Hello from AWS Lambda!')
    }
