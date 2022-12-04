from flask import Flask, render_template, request
import boto3
import scratchpad 

dbclient = boto3.resource("dynamodb")
searchdatabase = dbclient.Table("searchItems")


app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def UserInput():
    resp = scratchpad.query_table('searchItems', 'email', '222222')
    posts = resp.get('Items')
    print(posts)
    if request.method == "POST":
        if request.form.get('action1') == 'Add':
            print("userInput() Called!!!!!!!!!!!!!!!!!!!")
            searchword = request.form.get("searchword")
            searchURL = request.form.get("URL")
            response = scratchpad.put_info('222222', searchURL, searchword)
            print(response)
            print(searchword)
            print(searchURL)
    return render_template('index.html', posts=posts)


