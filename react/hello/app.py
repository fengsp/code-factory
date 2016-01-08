from flask import Flask
from flask import jsonify, render_template, request


app = Flask(__name__)


comments = [
    {"id": 1, "author": "Pete Hunt", "text": "This is one comment"},
    {"id": 2, "author": "Jordan Walke", "text": "This is *another*"},
]
current_id = 3


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/comments', methods=['GET', 'POST'])
def handle_comments():
    global comments
    global current_id
    if request.method == 'POST':
        author = request.form['author']
        text = request.form['text']
        comment = {
            'id': current_id,
            'author': author,
            'text': text,
        }
        comments.append(comment)
        current_id += 1
    return jsonify(comments=comments)


if __name__ == '__main__':
    app.run(debug=True)
