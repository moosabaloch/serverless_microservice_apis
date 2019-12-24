import json
import mysql.connector

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": mysql.connector.version.LICENSE
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
