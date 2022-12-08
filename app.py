from flask import Flask, render_template, request, redirect
import boto3
import scratchpad 
import time
import json

dbclient = boto3.resource("dynamodb")
searchdatabase = dbclient.Table("searchItems")


app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def UserInput():
    resp = scratchpad.query_table('searchItems', 'email', '222222')
    posts = resp.get('Items')
    # print(posts)
    # if request.method == "POST":
    #     if request.form.get('Add') == 'Add':
    #         print("userInput() Called!!!!!!!!!!!!!!!!!!!")
    #         searchword = request.form.get("searchword")
    #         searchURL = request.form.get("URL")
    #         response = scratchpad.put_info('222222', searchURL, searchword)
    #         print(response)
    #         print(searchword)
    #         print(searchURL)
    return render_template('index.html', posts=posts)

@app.route('/DeleteItem',  methods =["POST"])
def DeleteItem():
    information = request.data
    deleteThis = int(information.decode("utf-8"))
    # replace with email from login
    email = '222222'
    response = scratchpad.delete_info(email, deleteThis)
    print(response)
   
    resp = scratchpad.query_table('searchItems', 'email', '222222')
    posts = resp.get('Items')
    return render_template('index.html', posts=posts)

@app.route('/TestItem', methods = ["POST"])
def TestItem():
    information = request.data
    # information = request.form
    testThis = int(information.decode("utf-8"))

    # insert code to send a test email
    print('TestItem() called!!!! testThis= ', testThis)

    resp = scratchpad.query_table('searchItems', 'email', '222222')
    posts = resp.get('Items')
    return render_template('index.html', posts=posts)

@app.route('/AddItem', methods=["GET","POST"])
def AddItem():
    print("AddItem() Called")

    information = request.data
    testThis = (information.decode("utf-8"))
    data = json.loads(testThis)

    print("testThis= ", testThis)
    print("AddItem() data[item] = ", data["item"])
    print("AddItem() data[URL] = ", data["URL"])

    # searchword = request.form.get("searchword")
    # searchURL = request.form.get("URL")
    response = scratchpad.put_info('222222', data["URL"], data["item"])
    print(response)
    time.sleep(1)
    resp = scratchpad.query_table('searchItems', 'email', '222222')
    posts = resp.get('Items')
    
    return render_template('index.html', posts=posts)