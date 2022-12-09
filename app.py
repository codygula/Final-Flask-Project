from flask import Flask, render_template, request, redirect
import boto3
import scratchpad 
import time
import json
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import bcrypt

dbclient = boto3.resource("dynamodb")
searchdatabase = dbclient.Table("searchItems")


app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def UserInput():
    resp = scratchpad.query_table('searchItems', 'email', '222222')
    posts = resp.get('Items')
    return render_template('index.html', posts=posts)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	form = LoginForm()
# 	if form.validate_on_submit():
# 		user = Users.query.filter_by(username=form.username.data).first()
# 		if user:
# 			# Check the hash
# 			if check_password_hash(user.password_hash, form.password.data):
# 				login_user(user)
# 				flash("Login Succesfull!!")
# 				return redirect(url_for('dashboard'))
# 			else:
# 				flash("Wrong Password - Try Again!")
# 		else:
# 			flash("That User Doesn't Exist! Try Again...")


# 	return render_template('login.html', form=form)




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

    response = scratchpad.put_info('222222', data["URL"], data["item"])
    print(response)


    resp = scratchpad.query_table('searchItems', 'email', '222222')
    posts = resp.get('Items')
    
    return render_template('index.html', posts=posts)