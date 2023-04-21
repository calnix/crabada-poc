import boto3
import json


def get_pk():

    secret_name = SECRET_NAME
    region_name = "us-west-2"


    # Create a Secrets Manager client
    client = boto3.client(service_name='secretsmanager',region_name=region_name)

    # secretID is Secret name we set in aws |  will get dict as response
    response = client.get_secret_value(SecretId=secret_name)

    # access 'SecretString' from response
    # returns json object in the form of string |  convert json string to dict 
    secretDict = json.loads(response['SecretString'])
    account1_pk = secretDict['account1']

    return account1_pk

