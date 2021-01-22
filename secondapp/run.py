from flask import (Flask, request, Response, render_template, make_response, jsonify)
import boto3

app = Flask(__name__)


@app.route("/")
def hello():
    """GET in server"""
    response = Response("Running")
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/content")
def content():
    s3 = S3()
    result = s3.load()
    response = Response(result)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


class S3:
    def __init__(self):
        # ToDo 2
        self.s3 = boto3.client('s3',
                               aws_access_key_id='XXXXX',
                               aws_secret_access_key='XXXXX')

    def load(self):
        # ToDo 3
        response = self.s3.select_object_content(
            Bucket='XXXXX',
            Key='XXXXX',
            ExpressionType='SQL',
            Expression="SELECT s.Index FROM s3object s where (CAST(s.Height as FLOAT) > 75) and (CAST(s.Height as FLOAT) < 80 )",
            InputSerialization={
                    'CSV': {
                        'FileHeaderInfo': 'USE',
                        'RecordDelimiter': '\n',
                        'FieldDelimiter': ',',
                    }
            },
            OutputSerialization={
                'CSV': {
                    'RecordDelimiter': '|',
                    'FieldDelimiter': ',',
                }
            }
        )

        records = []

        for event in response['Payload']:
            if 'Records' in event:
                records.append(event['Records']['Payload'])
            elif 'Stats' in event:
                stats = event['Stats']['Details']
        return records[0]


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
