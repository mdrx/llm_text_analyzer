from flask import Flask, request, render_template, redirect, url_for, session
from flask_session import Session
from analyzer import get_response  # Update this import based on where you handle your logic
from references import *

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
sess = Session()
sess.init_app(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', systemprompts = systemprompts, models = availablemodels)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        text = request.form['text']
        requestedmodel = request.form['model']
        system_prompt = request.form['system_prompt']
        input_question = request.form['question']
        
        systemprompt = system_prompt
        try:
            response_object = get_response(content=text, question=input_question, model=requestedmodel, systemprompt=systemprompt)
            session['response_object'] = response_object
            return redirect(url_for('response'))
        except Exception as e:
            return str(e)  # For simplicity, just returning the exception as a string.


@app.route('/response')
def response():
    # Extract the result or handle it via session or other means
    response_object = session.get('response_object', 'No response found')
    if response_object is None:
        return redirect(url_for('/'))
    return render_template('response.html', response_object=response_object)

if __name__ == '__main__':
    app.run(debug=True)

