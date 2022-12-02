from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    posts = [
        {
        'title': 'test1',
        'created': 'test1'
    },
        {
        'title': 'test2',
        'created': 'test2'
    }]

    return render_template('index.html', posts=posts)
