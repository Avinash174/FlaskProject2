from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my project !'

@app.route('/hello')
def hello():
    return 'Hello All'

# Success link
@app.route('/success/<int:score>')
def success(score):
    return 'The person has passed. Marks: ' + str(score)

# Failed link
@app.route('/failed/<int:score>')
def fail(score):
    return 'The person has failed. Marks: ' + str(score)

# Result link
@app.route('/result/<int:marks>')
def result(marks):
    if marks < 40:
        return "<h1>redirect(url_for('fail', score=marks))</h1>"  # Redirect to 'fail' route
    else:
        return "<h2>redirect(url_for('success', score=marks))</h2>"  # Redirect to 'success' route

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
