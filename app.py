from flask import Flask, render_template
import boto3
import scratchpad 

dbclient = boto3.resource("dynamodb")
searchdatabase = dbclient.Table("searchItems")


app = Flask(__name__)

@app.route('/')
def index():


    # response = searchdatabase.get_item(
    # TableName="searchItems",
    # Key={
    #     "email": "222222",
    #     "ItemNumber": "*"
    # })
    # dbSearchTerm = response['Item']['searchterm']
    # dbURL = response['Item']['siteURL']
    # print(dbSearchTerm)
    # print(dbURL)

    resp = scratchpad.query_table('searchItems', 'email', '222222')
    posts = resp.get('Items')
    print(posts)
    # posts = [
    #     {
    #     'title': dbSearchTerm,
    #     'created': dbURL
    # },
    #     {
    #     'title': 'test2',
    #     'created': 'test2'
    # }]

    return render_template('index.html', posts=posts)
