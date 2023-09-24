from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

from script import ChatGpt

chat = ChatGpt()


app = Flask(__name__)


@app.route('/')
def home():
    args = request.args
    if 'query' in args:
        query = args['query']
        print(query)
        result = chat.answer_question(question=query)
        print(result)
        return render_template('./index.html', query = query, result = result)
    return render_template('./index.html')





app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.run(debug=True)