from flask import (Flask, request, render_template)
import mysql.connector
from decimal import Decimal
import json
import boto3
from boto3.dynamodb.conditions import Key
app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/rdsdb")
def test():
    storage = Storage()
    result = storage.load()
    print(result)
    return "Hello : " + result


@app.route("/dynamodb")
def load():
    dynamoDB = DynamoDB()
    result = dynamoDB.load()
    print(result)
    return "Hello :" + result[0]['ProductCategory']


class DynamoDB:
    def __init__(self):
        self.dynamodb = boto3.resource(
                # ToDo
                aws_access_key_id="x",
                aws_secret_access_key="x",
                service_name='dynamodb',
                region_name='x')
        self.table = self.dynamodb.Table('x')

    def load(self):
        response = self.table.query(
            KeyConditionExpression=Key('Id').eq(403)
        )
        return response['Items']


class Storage:

    def __init__(self):
        self.db = mysql.connector.connect(
            # ToDo
            user='x',
            passwd='x',
            db='x',
            host='x',
            port=3306
        )

    def load(self):
        cur = self.db.cursor()
        # ToDo
        cur.execute('''  ''')
        row = cur.fetchall()
        return row[0][1]


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
