from flask import Flask
from flask import jsonify, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/comments')
def get_comments():
    comments = [
        {"id": 1, "author": "Pete Hunt", "text": "This is one comment"},
        {"id": 2, "author": "Jordan Walke", "text": "This is *another*"},
    ]
    return jsonify(comments=comments)


if __name__ == '__main__':
    app.run()
