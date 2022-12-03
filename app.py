from flask import Flask, render_template, request
import boto3
import scratchpad 

dbclient = boto3.resource("dynamodb")
searchdatabase = dbclient.Table("searchItems")


app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def index():

    resp = scratchpad.query_table('searchItems', 'email', '222222')
    posts = resp.get('Items')
    print(posts)

    return render_template('index.html', posts=posts)



@app.route('/', methods =["GET", "POST"])
def UserInput():
    if request.method == "POST":
        searchword = request.form.get("searchword")
        searchURL = request.form.get("URL")

        print(searchword)
        print(searchURL)
    return render_template('index.html')



