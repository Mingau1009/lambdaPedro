import boto3
import os

def lambda_handler(event, context):
    ses = boto3.client('ses', region_name='us-east-1')

    response = ses.send_email(
        Source=os.environ['EMAIL_SOURCE'],
        Destination={'ToAddresses': [event['to_email']]},
        Message={
            'Subject': {'Data': event['subject']},
            'Body': {'Text': {'Data': event['body']}}
        }
    )

    return {
        'statusCode': 200,
        'body': f"Email enviado com sucesso: {response['MessageId']}"
    }
