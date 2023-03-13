from flask import Flask, render_template,request, redirect


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question1', methods=['GET', 'POST'])
def question1():
    if request.method == 'POST':
        response = request.form['response']
        if response == 'yes':
            return redirect('/question2a')
        else:
            return redirect('/question2b')
    return render_template('question1.html')

@app.route('/question2a', methods=['GET', 'POST'])
def question2a():
    if request.method == 'POST':
        response = request.form['response']
        if response == 'a':
            return redirect('/question3a1')
        else:
            return redirect('/question3a2')
    return render_template('question2a.html')

@app.route('/question2b', methods=['GET', 'POST'])
def question2b():
    if request.method == 'POST':
        response = request.form['response']
        if response == 'b':
            return redirect('/question3b1')
        else:
            return redirect('/question3b2')
    return render_template('question2b.html')

@app.route('/question3a1')
def question3a1():
    return render_template('question3a1.html')

@app.route('/question3a2')
def question3a2():
    return render_template('question3a2.html')

@app.route('/question3b1')
def question3b1():
    return render_template('question3b1.html')

@app.route('/question3b2')
def question3b2():
    return render_template('question3b2.html')
