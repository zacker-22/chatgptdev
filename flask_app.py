from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

from script import ChatGpt

chat = ChatGpt()


app = Flask(__name__)


@app.route('/')
def home():
    args = request.args
    if 'query' in args:
        query = args['query']
        result = chat.answer_question(question=query)
        return render_template('./index.html', query = query, result = result)
    return render_template('./index.html')


@app.route('/api')
def api():
    args = request.args
    if 'query' in args:
        query = args['query']
        result = chat.answer_question(question=query)
        print(jsonify({'query': query, 'result': result}))
        return jsonify({'query': query, 'result': result})
        
    
    return jsonify({'query': '', 'result': ''})


app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.run(debug=True, port=5000)