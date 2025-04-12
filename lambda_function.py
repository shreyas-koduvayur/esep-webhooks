import os
import json
import requests

def lambda_handler(event, context):
    try:
        issue_url = event['issue']['html_url']
        slack_url = os.environ['SLACK_URL']
        payload = {"text": f"Issue Created: {issue_url}"}
        response = requests.post(slack_url, json=payload)
        return {"statusCode": 200, "body": json.dumps("Success!")}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps(str(e))}