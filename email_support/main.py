import flask
import chatgpt as chat
app = flask.Flask(__name__)
chat = chat.ChatGpt()
@app.route('/', methods=['GET', 'POST'])
def home():
    if flask.request.method == 'POST':
        query = flask.request.form['query']
        result = chat.generate_email(query)

        print(query, result)
        return flask.render_template('./index.html', query = query, result = result)
    return flask.render_template('./index.html', query = '', result = '')


app.run(debug=True, port=5000)