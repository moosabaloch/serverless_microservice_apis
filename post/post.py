import json
import mysql.connector
import sls_util.rds_config as rds


def create(event, context):
    body = {
        "message": "API with python requirements",
        "my_sql_ver": mysql.connector.version.VERSION_TEXT,
        "Current Working Directory ": rds.test_connector()
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
