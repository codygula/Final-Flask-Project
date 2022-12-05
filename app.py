from flask import Flask, render_template, request
import boto3
import scratchpad 
import time

dbclient = boto3.resource("dynamodb")
searchdatabase = dbclient.Table("searchItems")


app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def UserInput():
    resp = scratchpad.query_table('searchItems', 'email', '222222')
    posts = resp.get('Items')
    print(posts)
    if request.method == "POST":
        if request.form.get('Add') == 'Add':
            print("userInput() Called!!!!!!!!!!!!!!!!!!!")
            searchword = request.form.get("searchword")
            searchURL = request.form.get("URL")
            response = scratchpad.put_info('222222', searchURL, searchword)
            print(response)
            print(searchword)
            print(searchURL)
    return render_template('index.html', posts=posts)

@app.route('/DeleteItem',  methods =["POST"])
def DeleteItem():
    information = request.data
    deleteThis = int(information.decode("utf-8"))
    email = '222222'
    print('DEBUG! ', type(deleteThis), deleteThis, email)
   
    response = scratchpad.delete_info(email, deleteThis)
    print(response)
   
    resp = scratchpad.query_table('searchItems', 'email', '222222')
    posts = resp.get('Items')
    return render_template('index.html', posts=posts)

@app.route('/TestItem', methods = ["POST"])
def TestItem():
    information = request.data
    print('information= ', information)
    print('information= ', str(information[0]))
    print('information= ', information[1])
    resp = scratchpad.query_table('searchItems', 'email', '222222')
    posts = resp.get('Items')
    return render_template('index.html', posts=posts)
